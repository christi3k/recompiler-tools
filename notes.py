from bs4 import BeautifulSoup

soup_out = BeautifulSoup('<ul id="show notes"></ul>', "lxml")

with open("test.nhsx") as fp:
    soup_in = BeautifulSoup(fp, "xml")

markers = soup_in.find_all('Marker')

ulist = soup_out.ul

print("now loop through markers")
for m in markers:
    if 'Type' in m.attrs and m['Type'] == 'Chapter':
        new_tag = soup_out.new_tag("a", href=m['URL'])
        ulist.append(new_tag)
        new_tag.string = m['Name']
        new_li = soup_out.new_tag("li")
        new_li.string = "["+m['Time'][:-4]+"] "
        new_tag.wrap(new_li)

print(ulist)
#print(soup_out.prettify())
