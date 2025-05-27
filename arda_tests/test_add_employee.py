import allure
from pages.add_employee_form import AddEmployeePage
import time


# @allure.epic("UI тесты")
# @allure.feature("Форма регистрации сотрудника")
# @allure.story("Проверка отправки пустой формы")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.tag("registration", "validation")
# @allure.label("owner", "Kuznetsova")
# def test_empty_employee_form_validation(setup_browser):
#     page = AddEmployeePage(setup_browser)
#
#     with allure.step("Открыть форму добавления сотрудника"):
#         page.open_add_form()
#
#     with allure.step("Нажать кнопку 'Отправить заявку' не заполняя поля"):
#         page.submit()
#
#     with allure.step("Проверить ошибки валидации у обязательных полей"):
#         page.should_see_error_by_field("email")
#         page.should_see_error_by_field("firstName")
#         page.should_see_error_by_field("lastName")
#         page.should_see_error_by_field("position")
#         page.should_see_error_by_field("password")
#         page.should_see_error_by_field("confirmPassword") TODO



@allure.epic("UI тесты")
@allure.feature("Форма добавления сотрудника")
@allure.story("Корректное добавление сотрудника")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("employee", "positive")
@allure.label("owner", "Kuznetsova")
def test_add_employee_with_valid_data(setup_browser):
    page = AddEmployeePage(setup_browser)
    unique_email = f"autotest_user_{int(time.time())}@fake-domain.test"

    with allure.step("Открыть форму добавления сотрудника"):
        page.open_add_form()
    with allure.step("Заполнить форму корректными данными"):
        page.select_company("Work Solutions")
        page.fill_email(unique_email)
        page.fill_first_name("Autotest")
        page.fill_last_name("User")
        page.fill_position("Test Engineer")
        page.fill_password("StrongPassword123")
        page.confirm_password("StrongPassword123")
    with allure.step("Отправить форму"):
        page.submit()
    with allure.step("Проверить сообщение об успешном добавлении"):
        page.should_see_success_message()



@allure.epic("UI тесты")
@allure.feature("Регистрация менеджера")
@allure.story("Невалидный пароль при регистрации")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("registration", "negative")
@allure.label("owner", "Kuznetsova")
@allure.epic("UI тесты")
@allure.feature("Регистрация менеджера")
@allure.story("Невалидный пароль при регистрации")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("registration", "negative")
@allure.label("owner", "Kuznetsova")
def test_manager_registration_with_invalid_password(setup_browser):
    page = AddEmployeePage(setup_browser)
    unique_email = f"autotest_manager_{int(time.time())}@fake-domain.test"

    with allure.step("Нажать кнопку 'Войти' и выбрать 'Регистрация для менеджеров'"):
        page.open_add_form()
    with allure.step("Выбрать компанию"):
        page.select_company("Work Solutions")
    with allure.step("Ввести корректные данные"):
        page.fill_email(unique_email)
        page.fill_first_name("Autotest")
        page.fill_last_name("Manager")
        page.fill_position("Test Manager")
    with allure.step("Ввести НЕВАЛИДНЫЙ пароль '111' и повторить его"):
        page.fill_password("111")
        page.confirm_password("111")
    with allure.step("Нажать кнопку 'Отправить заявку'"):
        page.submit()
    with allure.step("Проверить сообщение об ошибке валидации пароля"):
        # Для поля "Новый пароль" проверим ошибку длины
        # Предполагаем, что у поля имя "password"
        page.should_see_error_by_field("Новый пароль", "Длина пароля не менеее 6ти символов")
