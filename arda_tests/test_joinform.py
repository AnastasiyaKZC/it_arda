import allure
from pages.join_form import JoinClusterPage
from selene import be, have


@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Пользователь успешно отправляет форму")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "positive")
@allure.label("owner", "Kuznetsova")
def test_successful_join_cluster_submission(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму вступления в кластер"):
        join_page.open_join_form()

    with allure.step("Заполняем базовую информацию"):
        join_page.fill_basic_info(
            email="test@example.com",
            phone="+79998887766",
            name="Анна",
            last_name="Кузнецова",
            position="QA",
            company="TestCorp",
            site="https://testcorp.ru"
        )

    with allure.step("Отвечаем на вопросы и настраиваем слайдеры"):
        with allure.step("Выбираем 'Да' на вопрос 1"):
            join_page.select_question_1(yes=True)
        with allure.step("Устанавливаем значение слайдера 1 в 2"):
            join_page.set_slider_value(index=0, value=2)
        with allure.step("Выбираем 'Да' на вопрос 3"):
            join_page.select_question_3(yes=True)
        with allure.step("Устанавливаем значение слайдера 2 в 8"):
            join_page.set_slider_value(index=1, value=8)

    with allure.step("Соглашаемся с политикой конфиденциальности"):
        join_page.agree_to_privacy_policy()

    with allure.step("Отправляем форму"):
        join_page.submit()

    with allure.step("Проверяем сообщение об успешной отправке"):
        join_page.should_see_success_message()


@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Валидация при отправке пустой формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "negative")
@allure.label("owner", "Kuznetsova")
def test_join_cluster_validation_errors_on_empty_fields(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму вступления в кластер"):
        join_page.open_join_form()

    with allure.step("Оставляем поля пустыми (не заполняем)"):
        pass

    with allure.step("Выбираем 'Да' на вопрос 1"):
        join_page.select_question_1(yes=True)

    with allure.step("Устанавливаем значение слайдера 1 в 2"):
        join_page.set_slider_value(index=0, value=2)

    with allure.step("Выбираем 'Да' на вопрос 3"):
        join_page.select_question_3(yes=True)

    with allure.step("Устанавливаем значение слайдера 2 в 8"):
        join_page.set_slider_value(index=1, value=8)

    with allure.step("Оставляем чекбокс 'Я согласен' НЕвыбранным"):
        pass  # ничего не делаем

    with allure.step("Нажимаем кнопку 'Отправить заявку'"):
        join_page.submit()

    with allure.step("Проверяем сообщение об обязательном заполнении для всех полей"):
        fields = [
            "Введите почту",
            "Введите телефон",
            "Введите имя",
            "Введите фамилию",
            "Введите должность",
            "Введите название",
            "Укажите ссылку"
        ]

        for placeholder in fields:
            with allure.step(f"Проверяем ошибку для поля '{placeholder}'"):
                container = setup_browser.element(
                    f"//input[@placeholder='{placeholder}']/ancestor::div[contains(@class, 'flex') and contains(@class, 'flex-wrap') and contains(@class, 'mb-4') and contains(@class, 'w-full')]"
                )
                error_el = container.element("span.mt-2.text-red")
                error_el.should(be.visible).should(have.text("Поле обязательно к заполнению"))


@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Валидация: обязательное поле не заполнено (чекбокс п.1)")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "negative")
@allure.label("owner", "Kuznetsova")
def test_join_cluster_validation_missing_checkbox_1(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму вступления в кластер"):
        join_page.open_join_form()

    with allure.step("Заполняем базовую информацию"):
        join_page.fill_basic_info(
            email="valid@example.com",
            phone="+79998887766",
            name="Анна",
            last_name="Кузнецова",
            position="QA",
            company="TestCorp",
            site="https://testcorp.ru"
        )

    with allure.step("Оставляем без выбора чекбокс п.1 (Программисты составляют бОльшую долю...)"):
        pass  # НЕ отмечаем чекбокс

    with allure.step("Выставляем значение слайдера п.2 в 3"):
        join_page.set_slider_value(index=0, value=3)

    with allure.step("Выбираем 'Да' на вопрос п.3"):
        join_page.select_question_3(yes=True)

    with allure.step("Выставляем значение слайдера п.4 в 5"):
        join_page.set_slider_value(index=1, value=5)

    with allure.step("Соглашаемся с политикой конфиденциальности"):
        join_page.agree_to_privacy_policy()

    with allure.step("Отправляем форму"):
        join_page.submit()

    with allure.step("Проверяем сообщение об ошибке обязательного заполнения у чекбокса п.1"):
        # Просто ищем на странице span с текстом ошибки
        setup_browser.element("span.text-red").should(
            have.text("Поле обязательно к заполнению")
        ).should(be.visible)
