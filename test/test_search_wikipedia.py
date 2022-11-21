from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


def test_open_register_form():
    with step('Open register form'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_account_name')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/login_create_account_link')).click()


def test_search():
    with step('Search and verify for Microsoft'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'Microsoft'
        )
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))

    with step('Search and verify for BrowserStack'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).clear()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'BrowserStack'
        )
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))

