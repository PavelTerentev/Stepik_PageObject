import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=options)
    # browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()