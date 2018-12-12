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
    _username_field = 'username'
    _password_field = 'password'
    _login_button = "kc-login"
    _login_error = "//span[@class='kc-feedback-text']"
    _forgot_password = "//a[contains(text(),'Forgot Password?')]"
    _user_icon = "//span[@class='d-none d-md-flex']"
    _logout = "//span[contains(text(),'Logout')]"

    # Methods to perform actions on elements

    def enterUserName(self,username):
        self.sendKeys(username,self._username_field)
    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)
    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def checkLoginError(self):
        result1 = self.getElementAttributeValue("text",self._login_error,"xpath")
        return result1
        # Sorry, we were not able to identify your information in our system. Please try again, or if you recently changed your username or email address, please call 1 888 939 4852 for assistance.

    def clickForgotPassword(self):
        self.elementClick(self._forgot_password,'xpath')

    def verifyLoginSuccessful(self):
        userIconElement = self.waitForElement(self._user_icon,'xpath',30)
        result = self.isElementPresent(element=userIconElement)
        return result

    def verifyLoginFailure(self):
        result = self.isElementPresent(self._login_error,'xpath')
        return result

    def clickLogout(self):
        userDropDown = self.waitForElement(self._user_icon,'xpath',10,1)
        self.elementClick(element=userDropDown)
        self.elementClick(self._logout,'xpath')

    #Main Method
    def login(self,username='',password=''):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(self._logout,locatorType='xpath',pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
