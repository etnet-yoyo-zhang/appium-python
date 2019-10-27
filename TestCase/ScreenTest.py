
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.FirstOpenPage import FirstOpenPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ScreenTest(ParametrizedTestCase):
    def testFirstOpen(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/screen.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = FirstOpenPage(app)
        page.operate()
        page.checkPoint()



    @classmethod
    def setUpClass(cls):
        super(ScreenTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ScreenTest, cls).tearDownClass()
