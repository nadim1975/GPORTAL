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
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager

from selenium.webdriver.firefox.options import Options as ff_options #to run headless firefox
from selenium.webdriver.chrome.options import Options as chrome_options   #for running headless chrome
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
    def getHomeDirectory(self):
        home = str(Path.home())
        return home
    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration
       For Bamboo integration need to use the webdriver manager to install the webdrivers on runtime
       instead of using the path on local machine:
       https://github.com/SergeyPirogov/webdriver_manager

        Returns:
            'WebDriver Instance'
        """
        """"
        # Location where I save the drivers on my local machine
        chromeDriverLocation = "C:\\Users\\nhussein\\PycharmProjects\\chromedriver.exe"
        ffDriverLocation = "C:\\Users\\nhussein\\PycharmProjects\\geckodriver.exe"
        ieDriverLocation = "C:\\Users\\nhussein\\PycharmProjects\\IEDriverServer.exe"
        """

        if self.browser == "ie":
            # Set ie driver
            #os.environ["webdriver.ie.driver"] = ieDriverLocation
            #driver = webdriver.Ie(ieDriverLocation)
            #install IE driver to default path C:\Users\nhussein\.wdm\IEDriverServer\3.141.5\Win32
            driver = webdriver.Ie(IEDriverManager(os_type="win32").install())

        elif self.browser == "edge":
             #default installation folder C:\Users\nhussein\.wdm\MicrosoftWebDriver\latest\win
            driver = webdriver.Edge(EdgeDriverManager().install())

        elif self.browser == "ff":
            #driver = webdriver.Firefox()
            # default installation path C:\Users\nhussein\.wdm\geckodriver\v0.23.0\win64
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        elif self.browser == "ffdocker":
            #driver = webdriver.Firefox()
            capabilities = DesiredCapabilities.FIREFOX.copy()
            driver = webdriver.Remote("http://127.0.0.1:4446/wd/hub", capabilities)

        elif self.browser == "ffheadless":
            ffDriverLocation = "C:\TEMP\geckodriver.exe"
            webdriver.Firefox(executable_path=GeckoDriverManager().install(path="C:\TEMP"))
            options = ff_options()
            options.headless = True
            driver = webdriver.Firefox(options=options,
                                       executable_path=ffDriverLocation)

        elif self.browser == "chrome":
            # Set chrome driver
            #os.environ["webdriver.chrome.driver"] = chromeDriverLocation
            #driver = webdriver.Chrome(chromeDriverLocation)
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.set_window_size(1920, 1080)

        elif self.browser == "chromedocker":
            # Set chrome driver
            #driverLocation = "C:\\Users\\nhussein\\PycharmProjects\\selenium_workspace\\chromedriver.exe"
            #os.environ["webdriver.chrome.driver"] = chromeDriverLocation
            ####### THIS WILL USE DOCKER CONTAINER AND LAUNCH THE SCRIPT ON VNC ##########################3##########
            capabilities = DesiredCapabilities.CHROME.copy()
            #capabilities['platform'] = "WINDOWS"
            #capabilities['version'] = "10"
            capabilities['takesScreenshot'] = True
            driver = webdriver.Remote("http://127.0.0.1:4446/wd/hub", capabilities)
            driver.set_window_size(1920,1080)

        elif self.browser == "chromeheadless":
            chromeDriverLocation = "C:\TEMP\chromedriver.exe"
            webdriver.Chrome(ChromeDriverManager().install(path="C:\TEMP"))

            # To use the default driver installation path comment out the above 2 lines and uncomment the below 2 lines

            #webdriver.Chrome(ChromeDriverManager().install())
            #chromeDriverLocation = str(self.getHomeDirectory())+"\.wdm\chromedriver\\2.45\win32\chromedriver.exe"

            options = chrome_options()
            options.headless = True
            driver = webdriver.Chrome(chromeDriverLocation, chrome_options=options)

        elif self.browser == "mobile":
            # Select which device you want to emulate by uncommenting it
            # More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
            mobile_emulation = {
                "deviceName": "iPhone 6/7/8"
                # "deviceName": "iPhone 6/7/8 Plus"
                # "deviceName": "iPhone X"
                # "deviceName": "iPad"
                # "deviceName": "iPad Mini"
                # "deviceName": "iPad Pro"
                # "deviceName": "Nexus 10"
                # "deviceName": "Galaxy S III"
                # "deviceName": "Galaxy Note 3"
                # Or specify a specific build using the following two arguments
                # "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
                # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
            }
            # Define a variable to hold all the configurations we want
            options = chrome_options()
            # Add the mobile emulation to the chrome options variable
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
            chromeDriverLocation = "C:\TEMP\chromedriver.exe"
            webdriver.Chrome(ChromeDriverManager().install(path="C:\TEMP"))
            driver = webdriver.Chrome(chromeDriverLocation, chrome_options=options)

        else:
            #driver = webdriver.Firefox()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

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
        elif self.environment == 'dev':
            baseURL = "https://portal.dev.aws.wfscorp.com/"
        else:
            baseURL = "https://portal.qa.aws.wfscorp.com/"

        # Loading browser with App URL

        driver.get(baseURL)
        return driver