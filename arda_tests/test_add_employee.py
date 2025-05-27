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

