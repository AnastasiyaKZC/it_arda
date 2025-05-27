from selene import have, by, be

class AddEmployeePage:
    def __init__(self, browser):
        """Инициализация с браузером"""
        self.browser = browser

    def open_add_form(self):
        """Открыть форму добавления сотрудника"""
        self.browser.element("button.col-start-10.col-end-11.px-4.py-2.mr-5.font-bold").click()
        self.browser.element(
            '//button[@type="button" and contains(normalize-space(.), "Регистрация для менеджеров")]'
        ).should(be.visible).click()
        return self

    def select_company(self, company_name: str):
        """Выбрать компанию"""
        self.browser.element(".multiselect").click()
        self.browser.element(".multiselect__input").type(company_name)
        self.browser.element(by.xpath(f"//span[contains(text(),'{company_name}')]")).click()
        return self

    def fill_email(self, email: str):
        """Ввести почту"""
        self.browser.element("input[name='email']").type(email)
        return self

    def fill_first_name(self, first_name: str):
        """Ввести имя"""
        self.browser.element("input[name='firstName']").type(first_name)
        return self

    def fill_last_name(self, last_name: str):
        """Ввести фамилию"""
        self.browser.element("input[name='lastName']").type(last_name)
        return self

    def fill_position(self, position: str):
        """Ввести должность"""
        self.browser.element("input[name='position']").type(position)
        return self

    def fill_password(self, password: str):
        """Ввести новый пароль"""
        self.browser.element("input[name='password']").type(password)
        return self

    def confirm_password(self, password: str):
        """Повторить пароль"""
        self.browser.element("input[name='confirmPassword']").type(password)
        return self

    def submit(self):
        """Нажать кнопку отправки"""
        self.browser.element("button[type='submit']").click()
        return self

    def should_see_success_message(self, message: str = "Сотрудник успешно добавлен"):
        """Проверить сообщение об успехе"""
        self.browser.element(".success-message").should(have.text(message))
        return self

    def should_see_error_by_field(self, field_name: str, error_text: str = "Поле обязательно к заполнению"):
        """Проверить ошибку обязательного поля"""
        selector = f"input[name='{field_name}'] ~ span"
        self.browser.element(selector).should(be.visible).should(have.text(error_text))
        return self