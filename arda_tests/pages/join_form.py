from selene import have, by, be

class JoinClusterPage:
    def __init__(self, browser):
        self.browser = browser

    def open_join_form(self):
        # Нажать кнопку "Вступить" для открытия формы
        self.browser.element(by.text("Вступить")).click()
        return self

    def fill_basic_info(self, email, phone, name, last_name, position, company, site):
        # Заполнить базовые поля формы
        self.browser.element("input[placeholder='Введите почту']").type(email)
        self.browser.element("input[placeholder='Введите телефон']").type(phone)
        self.browser.element("input[placeholder='Введите имя']").type(name)
        self.browser.element("input[placeholder='Введите фамилию']").type(last_name)
        self.browser.element("input[placeholder='Введите должность']").type(position)
        self.browser.element("input[placeholder='Введите название']").type(company)
        self.browser.element("input[placeholder='Укажите ссылку']").type(site)
        return self

    def select_question_1(self, yes=True):
        # Выбрать ответ "Да" или "Нет" для первого вопроса
        text = 'Да' if yes else 'Нет'
        selector = f"//label[contains(., '{text}')]"
        self.browser.element(by.xpath(selector)).click()
        return self

    def select_question_3(self, yes=True):
        # Выбрать ответ "Да" или "Нет" для третьего вопроса (второй по счёту)
        text = 'Да' if yes else 'Нет'
        selector = f"(//label[contains(., '{text}')])[2]"
        self.browser.element(by.xpath(selector)).click()
        return self

    def set_slider_value(self, index: int, value: int):
        # Установить значение слайдера по индексу
        sliders = self.browser.all("input[type='range']")
        slider = sliders[index]
        self.browser.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            slider(), value
        )
        return self

    def agree_to_privacy_policy(self, force_click=False):
        # Отметить чекбокс политики конфиденциальности, если не отмечен или по принудительному клику
        checkbox = self.browser.element("input[type='checkbox']")
        if force_click:
            checkbox.click()
        else:
            if not checkbox.matching(be.selected):
                checkbox.click()
        return self

    def submit(self):
        # Находим кнопку "ОТПРАВИТЬ ЗАЯВКУ" и кликаем по ней
        button = self.browser.element(by.text("Отправить заявку"))
        button.should(be.visible).click()
        return self


    def should_see_success_message(self):
        self.browser.element(
            "#app > div > div.fixed.backdrop-blur-sm.left-0.top-0.z-50.bg-background.w-full.h-screen.overflow-auto.flex > div > div > div > p") \
            .should(have.text("Заявка на вступление в ARDA успешно отправлена"))

