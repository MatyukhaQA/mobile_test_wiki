import os

import pytest
from appium.webdriver import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser
from appium import webdriver


from utils import attachments


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    load_dotenv()
    options = {
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-DEMO",
            "sessionName": "BStack first_test"
        }
    }
    USER_NAME = os.getenv('USER_NAME')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{USER_NAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=options
    )
    browser.config.timeout = 4
    yield setup_browser
    attachments.add_video(browser)
    browser.quit()
