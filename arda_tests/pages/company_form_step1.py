from selene import have, be


class FirstStepForm:
    def __init__(self, browser):
        self.browser = browser

    def should_have_title(self):
        self.browser.element('h2:text("Базовая информация о компании")').should(be.visible)
        return self

    def fill_company_name(self, text):
        self.browser.element('input[placeholder="Введите название"]').set_value(text)
        return self

    def check_company_name_required_error(self):
        self.browser.element('label:has-text("Поле обязательно к заполнению")').should(be.visible)
        return self

    def select_city(self, city_name: str):
        self.browser.element('div.multiselect').click()
        self.browser.all('.multiselect__option').element_by(have.exact_text(city_name)).click()
        return self

    def fill_website(self, url: str):
        self.browser.element('input[placeholder="Сайт"]').set_value(url)
        return self

    def fill_description(self, text: str):
        self.browser.element('textarea[placeholder*="позиционирование"]').set_value(text)
        return self

    def fill_contacts(self, text: str):
        self.browser.element('textarea[placeholder*="сотрудничества"]').set_value(text)
        return self

    def fill_legal_info(self, text: str):
        self.browser.element('textarea[placeholder*="ИНН"]').set_value(text)
        return self

    def click_next(self):
        self.browser.element('span.w-full.relative.inline-block.px-8.py-3.text-sm.font-bold.tracking-widest.text-black.uppercase.border-2.border-current').click()
        return self