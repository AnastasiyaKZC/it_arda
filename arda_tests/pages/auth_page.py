from selene import be, have, by

class AuthPage:
    def __init__(self, browser):
        self.browser = browser

    def open_auth_form(self):
        # Нажимаем кнопку для открытия формы авторизации
        self.browser.element('button.px-4.py-2.mr-5.font-bold').click()
        return self

    def enter_email(self, email):
        # Вводим email
        self.browser.element('[placeholder="Введите логин"]').set_value(email)
        return self

    def enter_password(self, password):
        # Вводим пароль
        self.browser.element('[placeholder="Введите пароль"]').set_value(password)
        return self

    def submit(self):
        # Нажимаем кнопку "Войти"
        self.browser.element('button[type="submit"]').click()
        return self

    def should_see_auth_error(self, field: str, message: str):
        # Проверка текста ошибки авторизации под конкретным полем (email или password)
        field_xpath_map = {
            "email": '//*[@id="email"]/ancestor::div[contains(@class, "flex") and contains(@class, "flex-wrap")]',
            "password": '//*[@placeholder="Введите пароль"]/ancestor::div[contains(@class, "flex") and contains(@class, "flex-wrap")]'
        }

        self.browser.element(field_xpath_map[field]) \
            .element("span.text-red") \
            .should(have.text(message))

    def should_be_logged_in(self):
        # Проверка, что пользователь авторизовался
        self.browser.element(by.text('Выход')).should(be.visible)

    def click_forgot_password(self):
        # Нажимаем на кнопку "Забыли пароль"
        self.browser.element('button:has-text("Забыли пароль")').click()
        return self