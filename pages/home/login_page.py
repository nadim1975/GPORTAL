import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    # constructor method to pass values
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
    # Locators
    _login_link = "//div[@id='navbar']//a[@href='/sign_in']"
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = "commit"
    _user_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _login_error = "//div[contains(text(),'Invalid email or password.')]"
    _logout = "//div[@id='navbar']//a[@href='/sign_out']"

    # Methods to perform actions on elements

    def clickLoginLink(self):
        self.elementClick(self._login_link,'xpath')

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)
    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)
    def clickLoginButton(self):
        self.elementClick(self._login_button,'name')
    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._user_icon,'xpath')
        return result
    def verifyLoginFailure(self):
        result = self.isElementPresent(self._login_error,'xpath')
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginPageTitle(self,title):
        return self.verifyPageTitle(title)


    #Main Method
    def login(self,email='',password=''):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(self._logout,locatorType='xpath',pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
