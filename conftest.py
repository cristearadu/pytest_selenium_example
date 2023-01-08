import pytest

from settings import WEBSITE
from core_elements.logger import logg
from core_elements.custom_webdriver import CustomWebDriverChrome, CustomWebDriverFirefox


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome', help='type of webdriver to use for testing')


@pytest.fixture
def config(request):

    config = {}
    browsers = ['chrome', 'firefox']
    parser_options = ['browser']

    for parser_option in parser_options:
        attribute_from_cli = getattr(request.config.option, parser_option)
        if attribute_from_cli is not None:
            config[parser_option] = attribute_from_cli

    assert config['browser'] in browsers

    return config


@pytest.fixture
def driver(config):

    # Initialize the WebDriver instance
    if config['browser'] == 'chrome':
        driver = CustomWebDriverChrome()

    elif config['browser'] == 'firefox':
        driver = CustomWebDriverFirefox()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    driver.maximize_window()
    driver.get(WEBSITE)

    yield driver

    driver.close()


@pytest.fixture
def logger():
    yield logg
