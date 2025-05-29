import allure
from pages.auth_page import AuthPage
from pages.company_form_step1 import FirstStepForm
from pages.company_form_step2 import SecondStepForm

@allure.epic("UI тесты")
@allure.feature("Регистрация компании")
@allure.story("Заполнение базовой информации о компании и второго участника Telegram-чата")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("company", "positive")
@allure.label("owner", "Kuznetsova")
def test_fill_company_base_info(setup_browser, test_credentials):
    browser = setup_browser
    auth_page = AuthPage(browser)
    company_form = FirstStepForm(browser)
    second_participant_form = SecondStepForm(browser)

    with allure.step("Авторизуемся с корректными данными"):
        (
            auth_page
            .open_auth_form()
            .enter_email(test_credentials["identifier"])
            .enter_password(test_credentials["password"])
            .submit()
        )

    with allure.step("Заполнить поля формы базовой информации о компании"):
        company_form.fill_company_name("ООО Автотест Компания")
        company_form.select_city("Москва")
        company_form.fill_website("https://example.com")
        company_form.fill_description("Мы занимаемся автоматизацией тестирования")
        company_form.fill_contacts("Телефон: +7 (900) 123-45-67, Email: test@example.com")
        company_form.fill_legal_info("ООО «Автотест», ИНН 1234567890")

    with allure.step("Нажать кнопку 'ДАЛЬШЕ' на форме базовой информации"):
        company_form.click_next()

    with allure.step("Заполнить данные второго участника telegram-чата корректными значениями"):
        second_participant_form.fill_full_name("Иванов Иван Иванович")
        second_participant_form.fill_position("Менеджер проектов")
        second_participant_form.fill_email("ivanov@example.com")
        second_participant_form.fill_telegram("@ivanov_telegram")
#
#     # with allure.step("Нажать кнопку 'ДАЛЬШЕ' на форме второго участника"):
#     #     second_participant_form.click_next()
#     # не получается кликнуть, редактирую метод в классе todo (поправила метод в page object, но не успела проверить - лежит админка на тестовом контуре)