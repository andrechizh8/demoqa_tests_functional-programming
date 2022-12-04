import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_open():
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()

