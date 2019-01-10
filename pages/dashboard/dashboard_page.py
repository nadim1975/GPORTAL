import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
#from utilities.util import Util

class DashboardPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _notifications = "//img[@class='toolbar-logo']"
    _hamburger_icon = "//img[@class='toolbar-logo menu-icon']"
    _user_settings_icon = "//mat-icon[@class='d-none d-md-flex mat-icon material-icons']"
    _home_icon = "//a[@class='crumb home']"
    _dashboard = "//span[contains(text(),'Dashboard')]"
    _fuel = "fuel-finder"
    _fuel_orders = "//span[contains(text(),'Fuel Orders')]"
    _invoices = "//span[contains(text(),'Invoices')]"
    _rewards = "//span[contains(text(),'Rewards')]"
    _fuelorders_today = "//span[contains(text(),'Today')]"
    _fuelorders_next7 = "//span[contains(text(),'Next 7 Days')]"
    _fuelorders_next30 = "//span[contains(text(),'Next 30 Days')]"



    def clickHamburgerIcon(self):
        hamburgerIconElement = self.waitForElement(locator=self._hamburger_icon,
                                              locatorType="xpath", pollFrequency=1)
        self.elementClick(element=hamburgerIconElement)

    def navigateToDashboard(self):
        self.clickHamburgerIcon()
        self.elementClick(locator=self._dashboard, locatorType="xpath")

    def navigateToFuel(self):
        self.clickHamburgerIcon()
        self.elementClick(locator=self._fuel, locatorType="link")

    def navigateToFuelOrders(self):
        self.clickHamburgerIcon()
        self.elementClick(locator=self._fuel_orders, locatorType="xpath")

    def navigateToInvoices(self):
        self.clickHamburgerIcon()
        self.elementClick(locator=self._invoices,locatorType="xpath")

    def navigateToRewards(self):
        self.clickHamburgerIcon()
        self.elementClick(locator=self._rewards, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
        #self.elementClick(locator=self._user_settings_icon,locatorType="xpath")

    def navigateHome(self):
        self.elementClick(self._home_icon,'xpath')
        print('Navigating Home')

    def clickFuelOrdersToday(self):
        self.elementClick(self._fuelorders_today,'xpath')

    def clickFuelOrdersNext7(self):
        self.elementClick(self._fuelorders_next7, 'xpath')

    def clickFuelOrdersNext30(self):
        self.elementClick(self._fuelorders_next30, 'xpath')

    def validateOrdersUplift(self,date):
        if date == 'today':
           print(self.util.todaysDate('ddmmmyyyy'))