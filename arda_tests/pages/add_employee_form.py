from selene import have, by, be

class AddEmployeePage:
    def __init__(self, browser):
        self.browser = browser

def open_add_form(self):
    # Клик по кнопке "Войти"
    self.browser.element("button.col-start-10.col-end-11.px-4.py-2.mr-5.font-bold").click()
    # Клик по кнопке "Регистрация для менеджеров"
    self.browser.element(
        "button.block.w-full.underline.text-center.text-gray-700.hover\\:no-underline.hover\\:text-black") \
        .should(be.visible).click()

    return self