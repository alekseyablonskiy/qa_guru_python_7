import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'aleksey')
@allure.feature('тесты для гита')
@allure.story('с лямбда шагами')
@allure.link('https://github.com', name='Testing')
def test_with_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')
        browser.driver.maximize_window()

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('открывает таб issues'):
        s('#issues-tab').click()

    with allure.step('проверяем наличие issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)


browser.quit()