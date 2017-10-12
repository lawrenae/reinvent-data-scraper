from bs4 import BeautifulSoup
import sys
import utils

html_filename = './AWS re_Invent 2017.htm'
if (len(sys.argv) > 1):
    html_filename = sys.argv[1]

soup = utils.read_main_html(html_filename)

links = soup.findAll('a', attrs={'class':'openInPopup'})

for link in links:
    session_name = utils.get_session_name(link)
    venue = utils.get_venue(link)
    session_type = utils.get_session_type(link)
    session_time = utils.get_times(link)

    print(utils.print_row(session_name, venue, session_type, session_time))
