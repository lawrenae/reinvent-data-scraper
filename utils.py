from bs4 import BeautifulSoup

def read_main_html(filename):
    file = open(filename, 'r')
    html = file.read()
    soup = BeautifulSoup(html, "html.parser")
    file.close()

    return soup

def print_row(session_name, venue, session_type, session_time):
    return session_name + "|" \
           + venue + '|' \
           + session_type + '|' \
           + session_time

def get_times(link):
    result = "no times"
    sessionTimes = __getSessionTimesDiv(link)
    tooltip = sessionTimes.find('div', attrs={'class':'tooltip'})
    if tooltip:
        result = tooltip.next_sibling
    else:
        print('no tooltip')

    return result

def get_venue(link):
    result = "no venue"
    sessionTimes = __getSessionTimesDiv(link)
    venue = sessionTimes.find('span', attrs={'class':'sessionRoom'})
    if venue:
        result = venue.text[2:]
        result = result.strip()
    else:
        print('no venue')

    return result

def get_session_name(soup):
    result = 'No Name!!'
    abbreviation = soup.find('span', attrs={'class':'abbreviation'})
    title = soup.find('span', attrs={'class':'title'})

    if abbreviation and title:
        result = abbreviation.text + title.text

    return result

def get_session_type(link):
    result = 'No type!!'
    session_type = link.parent.find('small', attrs={'class':'type'})

    if session_type:
        result = session_type.text

    return result


# private methods

def __getSessionTimesDiv(link):
    return link.parent.parent.find('div', attrs={'class':'sessionTimes'})

def __get_profile_item(soup_detail, profile_item_id, default_result):
    result = default_result
    rows = soup_detail.findAll('div', attrs={'id':profile_item_id})
    if len(rows) > 0:
        input_row = rows[0].find('input')
        if input_row:
            result = input_row.next_sibling

    return result;
