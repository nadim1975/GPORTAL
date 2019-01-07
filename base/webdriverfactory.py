"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
################  IMPORT THIS TO RUN ON DOCKER ######################################
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

class WebDriverFactory():

    def __init__(self, browser,environment):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.environment = environment
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        #browser = self.browser.lower()
        if self.browser == "ie":
            # Set ie driver
            driverLocation = "C:\\Users\\nhussein\\PycharmProjects\\selenium_workspace\\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = driverLocation
            driver = webdriver.Ie(driverLocation)

        elif self.browser == "ff":
            #driver = webdriver.Firefox()
            capabilities = DesiredCapabilities.FIREFOX.copy()
            driver = webdriver.Remote("http://127.0.0.1:4446/wd/hub", capabilities)

        elif self.browser == "chrome":
            # Set chrome driver
            driverLocation = "C:\\Users\\nhussein\\PycharmProjects\\selenium_workspace\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
        ####### THIS WILL USE DOCKER CONTAINER AND LAUNCH THE SCRIPT ON VNC ##########################3##########
            capabilities = DesiredCapabilities.CHROME.copy()
            #capabilities['platform'] = "WINDOWS"
            #capabilities['version'] = "10"
            capabilities['takesScreenshot'] = True
            driver = webdriver.Remote("http://127.0.0.1:4446/wd/hub", capabilities)
            #driver = webdriver.Chrome(driverLocation)
            driver.set_window_size(1920,1080)
        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()

        #selecting the URL based on the environment param
        #env = self.environment.lower()
        if self.environment == 'qa':
            baseURL = "https://portal.qa.aws.wfscorp.com/"
        elif self.environment == 'test':
            baseURL = "https://portal.test.aws.wfscorp.com/"
        elif self.environment == 'future':
            baseURL = "https://portal.future.aws.wfscorp.com/"
        else:
            baseURL = "https://portal.qa.aws.wfscorp.com/"

        # Loading browser with App URL

        driver.get(baseURL)
        return driver