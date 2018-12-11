import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser,environment):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser,environment)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login('test@email.com', 'abcabc')
    #print("&&&&&&&&&&&  OneTime Setup Execution")

# return the driver
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--environment", help="Which URL to use for testing")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--environment")