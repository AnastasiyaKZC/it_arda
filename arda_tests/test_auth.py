import allure
import pytest
from selene import be
from pages.auth_page import AuthPage


@allure.epic("UI тесты")
@allure.feature("Форма авторизации")
@allure.story("Проверка отправки пустой формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("auth", "validation")
@allure.label("owner", "Kuznetsova")
def test_empty_auth_form(setup_browser):
    auth_page = AuthPage(setup_browser)

    with allure.step("Открываем форму и отправляем пустую"):
        auth_page.open_auth_form().submit()

    with allure.step("Проверяем сообщение об ошибке под полем логина"):
        auth_page.should_see_auth_error("email", "Поле обязательно к заполнению")

    with allure.step("Проверяем сообщение об ошибке под полем пароля"):
        auth_page.should_see_auth_error("password", "Поле обязательно к заполнению")


@allure.epic("UI тесты")
@allure.feature("Форма авторизации")
@allure.story("Негативные кейсы авторизации")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("auth", "negative")
@allure.label("owner", "Kuznetsova")
@allure.title("Ошибка: '{expected_error}'")
@pytest.mark.parametrize(
    "email, password, field, expected_error",
    [
        ("wrong@arda.digital", "111111", "email", "Такого пользователя не существует"),
        ("member@arda.digital", "wrongpassword", "password", "Введен неверный пароль"),
    ]
)
def test_invalid_auth_cases(setup_browser, email, password, field, expected_error):
    auth_page = AuthPage(setup_browser)

    with allure.step("Открываем форму и вводим логин и пароль"):
        (
            auth_page
            .open_auth_form()
            .enter_email(email)
            .enter_password(password)
            .submit()
        )

    with allure.step(f"Проверяем сообщение об ошибке под полем {field}"):
        auth_page.should_see_auth_error(field, expected_error)

@allure.epic("UI тесты")
@allure.feature("Форма авторизации")
@allure.story("Пользователь успешно авторизуется")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("auth", "positive")
@allure.label("owner", "Kuznetsova")
def test_successful_authorization(setup_browser, credentials):
    auth_page = AuthPage(setup_browser)

    with allure.step("Вводим корректные логин и пароль"):
        (
            auth_page
            .open_auth_form()
            .enter_email(credentials["identifier"])
            .enter_password(credentials["password"])
            .submit()
        )

    with allure.step("Проверяем наличие меню авторизованного пользователя"):
        setup_browser.element('button.w-auto.flex.justify-center.align-middle').should(be.visible)


import allure
from selene import be

@allure.epic("UI тесты")
@allure.feature("Форма авторизации")
@allure.story("Переход в личный кабинет после авторизации")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("auth", "navigation")
@allure.label("owner", "Kuznetsova")
def test_access_account_after_login(setup_browser, credentials):
    auth_page = AuthPage(setup_browser)

    with allure.step("Авторизуемся с корректными данными"):
        (
            auth_page
            .open_auth_form()
            .enter_email(credentials["identifier"])
            .enter_password(credentials["password"])
            .submit()
        )

    with allure.step("Переходим на главную страницу через логотип"):
        setup_browser.element('a[href="/"]').click()

    with allure.step("Нажимаем кнопку 'Личный кабинет' в шапке"):
        setup_browser.element('a[href="/account/main/"].font-bold').should(be.visible).click()

    with allure.step("Проверяем наличие меню авторизованного пользователя"):
        setup_browser.element('button.w-auto.flex.justify-center.align-middle').should(be.visible)