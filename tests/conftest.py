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
    lp.login('Portalaviation1', 'Welcome01')
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

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         # always add url to report
#         extra.append(pytest_html.extras.url('http://www.nadim.com/'))
#         extra.append(pytest_html.extras.text('some string', name='Nadim TEST'))
#         extra.image(image, mime_type='image/gif', extension='gif')
#         #extra.image("C:\\Users\\nhussein\\PycharmProjects\\Gportal\\screenshots\\Checking Error Msg.1545014327797.png")
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#         report.extra = extra