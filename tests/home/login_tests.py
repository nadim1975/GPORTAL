from pages.home.login_page import LoginPage
import unittest
from utilities.teststatus import Status
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)


    @pytest.mark.run(order=2)
    def test_validlogin(self):
        #print("######## execution of correct login")
        self.lp.login('portalaviation1', 'Welcome01')
        result1 = self.lp.verifyPageTitle("Global Portal")
        self.ts.mark(result1,'Title is correct')
        #self.lp.login('test@email.com','abcabc')
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result2,"Login was successful")
        self.ts.markFinal("Validating Login",result2,"Login was successful")


    @pytest.mark.run(order = 1)
    def test_invalidlogin(self):
         # The class Setup fixture will open the URL the first time
        #print("**********   Execution of wrong login")
        self.lp.logout()
        self.lp.login('portalaviation1','wrong')
        #result1 = self.lp.checkLoginError("Sorry, we were not able to identify your information in our system. Please try again, or if you recently changed your username or email address, please call 1 888 939 4852 for assistance.")
        result = self.lp.verifyLoginFailure()
        self.ts.mark(result,"Checking Error Msg")
     #   assert result == True
    #


