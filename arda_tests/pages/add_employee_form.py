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
        """Выбрать компанию из выпадающего списка"""
        self.browser.element(".multiselect").click()
        input_elem = self.browser.element(".multiselect__input")
        input_elem.type(company_name)
        # Ждём появления списка и выбираем первый элемент
        first_option = self.browser.all(".multiselect__option").first
        first_option.click()
        return self

    def fill_email(self, email: str):
        """Ввести почту"""
        self.browser.element("#email").type(email)
        return self

    def fill_first_name(self, first_name: str):
        """Ввести имя"""
        self.browser.element("input[placeholder='Введите имя']").type(first_name)
        return self

    def fill_last_name(self, last_name: str):
        """Ввести фамилию"""
        self.browser.element("input[placeholder='Введите фамилию']").type(last_name)
        return self

    def fill_position(self, position: str):
        """Ввести должность"""
        self.browser.element("input[placeholder='Введите должность']").type(position)
        return self

    def fill_password(self, password: str):
        """Ввести новый пароль"""
        input_elem = self.browser.element(
            "//div[label[contains(text(),'Новый пароль')]]//input[@type='password']"
        )
        input_elem.type(password)
        return self

    def confirm_password(self, password: str):
        """Повторить пароль"""
        input_elem = self.browser.element(
            "//div[label[contains(text(),'Повторите пароль')]]//input[@type='password']"
        )
        input_elem.type(password)
        return self

    def submit(self):
        """Нажать кнопку отправки"""
        self.browser.element(
            "//button[@type='submit' and .//span[contains(@class, 'bg-orange')] and contains(., 'Отправить заявку')]"
        ).click()
        return self

    def should_see_success_message(self):
        # Проверяем, что есть <h2> с нужным текстом
        self.browser.element("h2.text-2xl.font-semibold.mb-3").should(have.text("Спасибо за регистрацию!"))

    def should_see_error_by_field(self, field_name: str, error_text: str = "Поле обязательно к заполнению"):
        """Проверить ошибку обязательного поля"""
        selector = f"input[name='{field_name}'] ~ span"
        self.browser.element(selector).should(be.visible).should(have.text(error_text))
        return self