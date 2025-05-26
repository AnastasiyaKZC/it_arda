from selene import have, by
import allure

class JoinClusterPage:
    def __init__(self, browser):
        self.browser = browser

    def open_join_form(self):
        with allure.step("Нажимаем кнопку 'Вступить' для открытия формы"):
            self.browser.element(by.text("Вступить")).click()
            allure.attach(
                self.browser.driver.get_screenshot_as_png(),
                name="Форма вступления",
                attachment_type=allure.attachment_type.PNG
            )
        return self

    def fill_basic_info(self, email, phone, name, last_name, position, company, site):
        self.browser.element("input[placeholder='Введите почту']").type(email)
        self.browser.element("input[placeholder='Введите телефон']").type(phone)
        self.browser.element("input[placeholder='Введите имя']").type(name)
        self.browser.element("input[placeholder='Введите фамилию']").type(last_name)
        self.browser.element("input[placeholder='Введите должность']").type(position)
        self.browser.element("input[placeholder='Введите название']").type(company)
        self.browser.element("input[placeholder='Укажите ссылку']").type(site)
        return self

    def select_question_1(self, yes=True):
        text = 'Да' if yes else 'Нет'
        # Ищем label с текстом Да или Нет и кликаем по нему
        selector = f"//label[contains(., '{text}')]"
        self.browser.element(by.xpath(selector)).click()
        return self

    def select_question_3(self, yes=True):
        selector = "(//label[contains(., 'Да')]/preceding-sibling::input[@type='checkbox'])[2]" if yes else "(//label[contains(., 'Нет')]/preceding-sibling::input[@type='checkbox'])[2]"
        self.browser.element(by.xpath(selector)).click()
        return self

    def set_slider_value(self, index: int, value: int):
        sliders = self.browser.all("input[type='range']")
        slider = sliders[index]
        self.browser.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            slider(), value
        )
        return self

    def agree_to_privacy_policy(self):
        self.browser.element("input[type='checkbox']").click()
        return self

    def submit(self):
        self.browser.element(by.text("ОТПРАВИТЬ ЗАЯВКУ")).click()
        return self

    def should_see_success_message(self):
        self.browser.should(have.text("Спасибо за заявку")) #адаптировать под реальность
        return self