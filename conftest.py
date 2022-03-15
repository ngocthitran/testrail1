import pytest, logging, sys, os
from datetime import *
from collections import namedtuple
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import consts

is_jenkins = False


def pytest_addoption(parser):
    parser.addoption("--jenkins", action="store", default=False)


def pytest_generate_tests(metafunc):
    global is_jenkins
    option_value = metafunc.config.option.jenkins
    if option_value is not None:
        is_jenkins = option_value


# Can change driver or have multiple driver here if needed
@pytest.fixture(params=["chrome"], scope="function")
def driver_init(request):
    options = None
    if request.param == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        if is_jenkins:
            print("Run on Jenkins with Chrome headless.")
            options.add_argument('disable-infobars')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-gpu')
            options.add_argument("--headless")
        else:
            print("Run on local dev/debug with Chrome")
        options.add_argument('start-maximized')
        options.add_argument("window-size=1366,768")
        web_driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        web_driver.implicitly_wait(30)
    request.cls.driver = web_driver
    yield
    for handle in web_driver.window_handles:
        web_driver.switch_to.window(handle)
        web_driver.close()


@pytest.fixture(scope="class")
def logger_init(request):
    logger = logging.getLogger(request.cls.__name__)

    c_handler = logging.StreamHandler(sys.stderr)
    c_handler.setLevel(logging.INFO)

    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)

    logger.addHandler(c_handler)
    request.cls.logger = logger


@pytest.fixture(scope="class")
def credentials_init(request):
    credentials = {
        "email": "sophia.tran+autonomar@revinate.com",
        "password": "Traninc@123"
    }

    credentials1 = {
        "email": "sophia.tran+autonomar@revinate.com",
        "password": "Traninc@123"
    }

    request.cls.credentials = namedtuple('Struct', credentials.keys())(*credentials.values())
    request.cls.credentials = namedtuple('Struct', credentials1.keys())(*credentials1.values())
