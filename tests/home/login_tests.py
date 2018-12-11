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
        self.lp.login('test@email.com', 'abcabc')
        result1 = self.lp.verifyLoginPageTitle("Let's Kode It")
        self.ts.mark(result1,'Title is not correct')
        #self.lp.login('test@email.com','abcabc')
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result2,"Login was successful")
        self.ts.markFinal("Validating Login",result2,"Login was successful")


    @pytest.mark.run(order = 1)
    def test_invalidlogin(self):
         # The class Setup fixture will open the URL the first time
        #print("**********   Execution of wrong login")
        self.lp.logout()
        self.lp.login('test@email.com','abc')
        result = self.lp.verifyLoginFailure()
        self.ts.mark(result,"Couldn't login with wrong userid/password")
     #   assert result == True
    #


