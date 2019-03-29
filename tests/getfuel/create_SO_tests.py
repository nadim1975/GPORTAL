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
        #if stuck in the request fuel window then close it
        self.so.clickCloseRequest()
        self.db.navigateHome()

    @pytest.mark.run(order=1)
    #@data(("JavaScript for beginners","4143202652384595","1220","101"),("Learn Python 3 from scratch","41426543764387900","1221","303"))
    #you can provide with only with the file name without the path since it is saved under the project
    #@data(*getCSVData("/Users/nhussein/PycharmProjects/Gportal/createSO_testdata.csv"))
    @data(*getCSVData("createSO_testdata.csv"))
    @unpack
    def test_validateSoCreation(self,icao,airportName,tailNumber,nextDestination,quantity,flightNumber,
                             arrivalDate,arrivalHour,arrivalMin,departureDate,departureHour,departureMin,notes,email,fax,phone):

        self.so.enterICAO(icao,airportName)

        self.so.selectLocation()
        self.so.selectFBOSetup()

        self.so.enterSoInformation(tailNumber,nextDestination,quantity,flightNumber,
                             arrivalDate,arrivalHour,arrivalMin,departureDate,departureHour,departureMin,notes,email,fax,phone)

        self.so.clickRequestFuel()
        # self.so.getQuoteNumber()
        # self.so.getSoNumber()
        result = self.so.verifySOcreated()
        self.ts.markFinal("test_SO_creation", result,
                          "SO Created Successfully")
