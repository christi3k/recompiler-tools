import argparse
import os
import logging
from bs4 import BeautifulSoup

# initiate argument parser
parser = argparse.ArgumentParser(description='Generate show notes from Hindenburg project files.')
parser.add_argument("input_file", help="Input filename.")

# check to see that file exists; exit with warning if not.
def file_exists_or_exit(file):
    if(not os.path.exists(file)):
        logging.warning('Cannot find input file %s. Exiting...', file)
        exit()
    else:
        logging.info('Found input file %s.', file)

# main function
if __name__ == '__main__':

    # setup logging
    logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO)
    logging.captureWarnings(True)

    # get command line arguments
    args = parser.parse_args()
    logging.debug(args)

    file_exists_or_exit(args.input_file)

    soup_out = BeautifulSoup('<ul id="show notes"></ul>', "lxml")

    with open(args.input_file) as fp:
        soup_in = BeautifulSoup(fp, "xml")

    markers = soup_in.find_all('Marker')

    ulist = soup_out.ul

    text_output = "\n\n"

    logging.info('Now looping through Chapter markers.')
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
