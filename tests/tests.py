import unittest
import sys
from bs4 import BeautifulSoup

sys.path.insert(0, ".")
import utils

class TestMainPage(unittest.TestCase):
    # with self.assertRaises(TypeError):
    def setUp(self):
        self.soup = utils.read_main_html('./AWS re_Invent 2017.htm')
        links = self.soup.findAll('a', attrs={'class':'openInPopup'})
        self.link = links[0]

    def test_read_file(self):
        self.assertNotEqual(None, self.soup)

    def test_getsession_name(self):
        session_name = utils.get_session_name(self.link)
        self.assertEqual(session_name, 'ENT302 - Optimizing Costs as You Scale on AWS')

    def test_get_venue(self):
        venue = utils.get_venue(self.link)
        self.assertEqual(venue, 'MGM, Level 1, Grand Ballroom 111')

    def test_get_session_type(self):
        session_type = utils.get_session_type(self.link)
        self.assertEqual(session_type, 'Breakout Session')

    def test_get_times(self):
        times = utils.get_times(self.link)
        self.assertEqual(times, 'Monday, Nov 27, 10:00 AM - 11:00 AM')


class TestPrinting(unittest.TestCase):
    def test_print_format(self):
        session_name = 'name'
        venue = 'venue'
        session_type = 'type'
        session_time = 'time'

        println = utils.print_row(session_name, venue, session_type, session_time)

        self.assertEqual(println, 'name|venue|type|time')


if __name__ == '__main__':
    unittest.main()
