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

    with allure.step("Заполняем корректные данные"):
        join_page.fill_basic_info(
            email="autotest_user@fake-domain.test",
            phone="+79990000000",
            name="Autotest",
            last_name="User",
            position="Test Engineer",
            company="Autotest Corp",
            site="https://autotest.fake"
        )

    with allure.step("Отмечаем чекбокс п.1"):
        join_page.select_question_1(yes=True)

    with allure.step("Выставляем значение слайдера п.2 в 2"):
        join_page.set_slider_value(index=0, value=2)

    with allure.step("Отмечаем чекбокс п.3"):
        join_page.select_question_3(yes=True)

    with allure.step("Выставляем значение слайдера п.4 в 8"):
        join_page.set_slider_value(index=1, value=8)

    with allure.step("Соглашаемся с политикой конфиденциальности"):
        join_page.agree_to_privacy_policy()

    with allure.step("Отправляем форму"):
        join_page.submit()

    with allure.step("Проверяем успешное сообщение"):
        join_page.should_see_success_message()



@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Валидация при отправке пустой формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "negative")
@allure.label("owner", "Kuznetsova")
def test_join_cluster_validation_errors_on_empty_fields(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму"):
        join_page.open_join_form()

    with allure.step("Отмечаем чекбокс п.1"):
        join_page.select_question_1(yes=True)

    with allure.step("Выставляем слайдер п.2 в 2"):
        join_page.set_slider_value(index=0, value=2)

    with allure.step("Отмечаем чекбокс п.3"):
        join_page.select_question_3(yes=True)

    with allure.step("Выставляем слайдер п.4 в 8"):
        join_page.set_slider_value(index=1, value=8)

    with allure.step("Отправляем пустую форму"):
        join_page.submit()

    with allure.step("Проверяем ошибки валидации для обязательных полей"):
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
            with allure.step(f"Проверяем поле '{placeholder}'"):
                container = setup_browser.element(
                    f"//input[@placeholder='{placeholder}']/ancestor::div[contains(@class, 'flex') and contains(@class, 'flex-wrap') and contains(@class, 'mb-4') and contains(@class, 'w-full')]"
                )
                container.element("span.mt-2.text-red") \
                    .should(be.visible) \
                    .should(have.text("Поле обязательно к заполнению"))


@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Валидация: обязательное поле не заполнено (чекбокс п.1)")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "negative")
@allure.label("owner", "Kuznetsova")
def test_join_cluster_validation_missing_checkbox_1(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму"):
        join_page.open_join_form()

    with allure.step("Заполняем корректные данные"):
        join_page.fill_basic_info(
            email="autotest_user@fake-domain.test",
            phone="+79990000000",
            name="Autotest",
            last_name="User",
            position="Test Engineer",
            company="Autotest Corp",
            site="https://autotest.fake"
        )

    with allure.step("Пропускаем чекбокс п.1"):
        pass

    with allure.step("Выставляем слайдер п.2 в 3"):
        join_page.set_slider_value(index=0, value=3)

    with allure.step("Отмечаем чекбокс п.3"):
        join_page.select_question_3(yes=True)

    with allure.step("Выставляем слайдер п.4 в 5"):
        join_page.set_slider_value(index=1, value=5)

    with allure.step("Соглашаемся с политикой конфиденциальности"):
        join_page.agree_to_privacy_policy()

    with allure.step("Отправляем форму"):
        join_page.submit()

    with allure.step("Проверяем ошибку валидации чекбокса п.1"):
        setup_browser.element(
            "//span[text()='Поле обязательно к заполнению' and contains(@class, 'text-red')]"
        ).should(have.text("Поле обязательно к заполнению")) \
            .should(be.visible)


@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Валидация: обязательное поле не заполнено (чекбокс п.3)")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "negative")
@allure.label("owner", "Kuznetsova")
def test_join_cluster_validation_missing_checkbox_3(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму"):
        join_page.open_join_form()

    with allure.step("Заполняем корректные данные"):
        join_page.fill_basic_info(
            email="autotest_user@fake-domain.test",
            phone="+79990000000",
            name="Autotest",
            last_name="User",
            position="Test Engineer",
            company="Autotest Corp",
            site="https://autotest.fake"
        )

    with allure.step("Отмечаем чекбокс п.1"):
        join_page.select_question_1(yes=True)

    with allure.step("Выставляем слайдер п.2 в 3"):
        join_page.set_slider_value(index=0, value=3)

    with allure.step("Пропускаем чекбокс п.3"):
        pass

    with allure.step("Выставляем слайдер п.4 в 7"):
        join_page.set_slider_value(index=1, value=7)

    with allure.step("Соглашаемся с политикой конфиденциальности"):
        join_page.agree_to_privacy_policy()

    with allure.step("Отправляем форму"):
        join_page.submit()

    with allure.step("Проверяем ошибку валидации чекбокса п.3"):
        setup_browser.element(
            "//span[text()='Поле обязательно к заполнению' and contains(@class, 'text-red')]"
        ).should(have.text("Поле обязательно к заполнению")).should(be.visible)


@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Валидация: не выбран чекбокс согласия с политикой конфиденциальности")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "negative")
@allure.label("owner", "Kuznetsova")
def test_join_cluster_validation_missing_privacy_checkbox(setup_browser):
    join_page = JoinClusterPage(setup_browser)

    with allure.step("Открываем форму вступления в кластер"):
        join_page.open_join_form()

    with allure.step("Заполняем корректные данные в поля формы"):
        join_page.fill_basic_info(
            email="autotest_user@fake-domain.test",
            phone="+79990000000",
            name="Autotest",
            last_name="User",
            position="Test Engineer",
            company="Autotest Corp",
            site="https://autotest.fake"
        )

    with allure.step("Отмечаем чекбокс п.1"):
        join_page.select_question_1(yes=True)

    with allure.step("Выставляем значение слайдера п.2 в 4"):
        join_page.set_slider_value(index=0, value=4)

    with allure.step("Отмечаем чекбокс п.3"):
        join_page.select_question_3(yes=True)

    with allure.step("Выставляем значение слайдера п.4 в 6"):
        join_page.set_slider_value(index=1, value=6)

    with allure.step("Снимаем отметку согласия с политикой конфиденциальности"):
        join_page.agree_to_privacy_policy(force_click=True)  # снимаем чекбокс

    with allure.step("Отправляем форму"):
        join_page.submit()

    with allure.step("Проверяем ошибку валидации чекбокса согласия"):
        container = setup_browser.element(
            "//span[text()='Поле обязательно к заполнению']/ancestor::div[contains(@class, 'mb-4')]"
        )
        container.element("span.text-red") \
            .should(have.text("Поле обязательно к заполнению")) \
            .should(be.visible)