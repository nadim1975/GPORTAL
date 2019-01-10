from pages.getfuel.create_SO_page import CreateSalesOrderPage
from pages.dashboard.dashboard_page import DashboardPage
from utilities.teststatus import Status
import unittest
import pytest
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RequestFuelTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.so = CreateSalesOrderPage(self.driver)
        self.ts = Status(self.driver)
        self.db = DashboardPage(self.driver)

    def setUp(self):
        self.db.navigateHome()

    @pytest.mark.run(order=1)

    @data(*getCSVData("/Users/nhussein/PycharmProjects/Gportal/dashboard_testdata.csv"))
    @unpack
    def test_validate_dashboard_links_656(self,icao,airportName):

        #validate quick fuel query
        self.so.enterICAO(icao,airportName)
        #back to Dashboard/Home
        self.db.navigateHome()
        #click fuel orders today
        self.db.clickFuelOrdersToday()
        #validate orders
        self.db.validateOrdersUplift('today')


        '''result = self.so.verifySOcreated()
        self.ts.markFinal("test_SO_creation", result,
                          "SO Created Successfully")
        '''


