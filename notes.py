from bs4 import BeautifulSoup

soup_out = BeautifulSoup('<ul id="show notes"></ul>', "lxml")

with open("ep55.nhsx") as fp:
    soup_in = BeautifulSoup(fp, "xml")

markers = soup_in.find_all('Marker')

ulist = soup_out.ul

text_output = "\n\n"

print("now loop through markers")
for m in markers:
    if 'Type' in m.attrs and m['Type'] == 'Chapter' and 'URL' in m.attrs:
        new_tag = soup_out.new_tag("a", href=m['URL'])
        ulist.append(new_tag)
        new_tag.string = m['Name']
        new_li = soup_out.new_tag("li")
        new_li.string = "["+m['Time'][:-4]+"] "
        new_tag.wrap(new_li)

        text_output += "- ["+m['Time'][:-4]+"] " + m['Name'] + ": " + m['URL'] + "\n"

print(ulist)
print(text_output)
#print(soup_out.prettify())
