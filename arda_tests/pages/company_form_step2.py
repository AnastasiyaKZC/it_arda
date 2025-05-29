from selene import have, be


class SecondStepForm:
    def __init__(self, browser):
        self.browser = browser

    def fill_full_name(self, full_name: str):
        self.browser.element('[placeholder="Введите ФИО"]').set_value(full_name)
        return self

    def fill_position(self, position: str):
        self.browser.element('input[placeholder="Введите должность"]').set_value(position)
        return self

    def fill_email(self, email: str):
        self.browser.element('input[placeholder="Введите почту"]').set_value(email)
        return self

    def fill_telegram(self, telegram: str):
        self.browser.element('input[placeholder="Введите username"]').set_value(telegram)
        return self

    def click_skip(self):
        self.browser.element('span').with_text("Пропустить").click()
        return self

    # def click_next(self):
    #     self.browser.element('span.w-full.relative.inline-block.px-8.py-3.text-sm.font-bold.tracking-widest.text-black.uppercase.border-2.border-current').click()
    #     return self todo