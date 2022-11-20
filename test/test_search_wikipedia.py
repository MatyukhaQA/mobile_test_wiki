from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


def test_search():

    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'QA'
        )

    with step('Content should be found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))
