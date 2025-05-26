import allure
from pages.join_form import JoinClusterPage

@allure.epic("UI тесты")
@allure.feature("Форма вступления в кластер")
@allure.story("Пользователь успешно отправляет форму")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("form", "positive")
@allure.label("owner", "Kuznetsova")
#
# def test_successful_join_cluster_submission(setup_browser):
#     join_page = JoinClusterPage(setup_browser)
#     join_page.open_join_form()
#
#     with allure.step("Заполняем форму и отправляем"):
#         join_page.fill_basic_info(
#             email="test@example.com",
#             phone="+79998887766",
#             name="Анна",
#             last_name="Кузнецова",
#             position="QA",
#             company="TestCorp",
#             site="https://testcorp.ru"
#         ).select_question_1(yes=True) \
#          .set_slider_value(index=0, value=2) \
#          .select_question_3(yes=True) \
#          .set_slider_value(index=1, value=8) \
#          .agree_to_privacy_policy() \
#          .submit()
#
#     with allure.step("Проверяем сообщение об успешной отправке"):
#         join_page.should_see_success_message()

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