import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver import FirefoxOptions


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    print("preparing settings for the code executing")
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 6.0
    browser.config.window_width = 1900
    browser.config.window_height = 950
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'

    browser.config.driver_options = driver_options

    yield

    browser.quit()
