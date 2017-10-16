import unittest
import sys
from bs4 import BeautifulSoup

sys.path.insert(0, ".")
import utils

class TestMainPage(unittest.TestCase):
    def setUp(self):
        raw_html = """
            <div id="sessionsTab" aria-labelledby="ui-id-8" class="ui-tabs-panel ui-widget-content ui-corner-bottom" role="tabpanel" aria-expanded="true" aria-hidden="false">

                    <div id="session_14490" class="resultRow sessionRow ">
                        <div class="detailColumn">

                            <a href="sessionDetail.ww?SESSION_ID=14490" class="openInPopup">

                                <span class="abbreviation">ENT302 - </span>

                                <span class="title">Optimizing Costs as You Scale on AWS</span>
                            </a>

                                <span class="abstract truncatedTxt">The cloud offers a first-in-a-career-opportunity to constantly optimize your costs as you grow and stay on the bleeding edge of innovation. By developing a cost-conscious... <a href="javascript:void(0);" class="moreLink truncated">View More</a></span>



                                <small class="type">Breakout Session</small>


                            <span class="scheduleStatus">




                            </span>
                        </div>
                        <div class="actionColumn">

                            <div class="sessionTimes">
                                <a href="javascript:void(0);" class="expandSessionImg expanded"><span class="ww-icon ww-icon-carrot-e"></span>Scheduling Options</a>
                                <ul class="availableSessions sessionTimeList" style="display: block;"><li><div class="tooltip">Session enrollment has not yet begun.<br></div>Monday, Nov 27, 10:00 AM - 11:00 AM<span class="sessionRoom"> – MGM, Level 1, Grand Ballroom 111</span></li></ul>
                            </div>

                            <a href="javascript:void(0);" class="interest interested"><span class="ww-icon ww-icon-star"></span>I'm no longer interested</a>


                        </div>
                    </div>
    """


        self.soup = BeautifulSoup(raw_html, 'html.parser')
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
