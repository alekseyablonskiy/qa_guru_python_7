import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'aleksey')
@allure.feature('тесты для гита')
@allure.story('с декораторами')
@allure.link('https://github.com')
def test_with_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step('отрываем главную страницу гита')
def open_main_page():
    browser.open('https://github.com')
    browser.driver.maximize_window()


@allure.step('ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('открываем там issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('проверяем наличие issue с номер {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)


browser.quit()