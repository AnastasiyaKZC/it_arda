import logging
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
import os
import pytest
from selene.core._browser import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

# Загружаем .env
load_dotenv()

@pytest.fixture(scope="session")
def credentials():
    identifier = os.getenv("IDENTIFIER")
    password = os.getenv("PASSWORD")

    if not identifier or not password:
        raise EnvironmentError("Не заданы переменные IDENTIFIER или PASSWORD в .env")

    return {
        "identifier": identifier,
        "password": password
    }

# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.INFO)
if not logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

@pytest.fixture(scope="session")
def base_url():
    return "https://it.arda.digital"
    # return "https://arda.ws-dev.ru/"

def log_request_and_response(response):
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Headers: {response.headers}")
    logger.info(f"Response Body (partial): {response.text[:200]}...")

    # Allure attachments
    allure.attach("Request URL", response.request.url, AttachmentType.TEXT)
    allure.attach("Request Method", response.request.method, AttachmentType.TEXT)
    allure.attach("Request Headers", str(response.request.headers), AttachmentType.TEXT)
    allure.attach("Response Status Code", str(response.status_code), AttachmentType.TEXT)
    allure.attach("Response Headers", str(response.headers), AttachmentType.TEXT)
    allure.attach("Response Body", response.text, AttachmentType.JSON)


# @pytest.fixture(scope='function')
# def setup_browser():
#     """Настраивает и возвращает браузер в selenoid перед тестами."""
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", "128.0")
#     options.set_capability("selenoid:options", {
#         "enableVNC": True,
#         "enableVideo": True
#     })
#     options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
#
#     print("🟡 Используем удаленный веб-драйвер через Selenoid")  # Проверка
#
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#     browser = Browser(Config(driver=driver))
#     yield browser
#
#     attach.add_screenshot(browser)
#     attach.add_html(browser)
#     attach.add_logs(browser)
#     attach.add_video(browser)
#     browser.quit()

@pytest.fixture(scope='function')
def setup_browser(base_url):
    """Настраивает и возвращает браузер в selenoid перед тестами."""
    options = Options()
    # Запускаем локальный браузер
    driver = webdriver.Chrome(options=options)
    browser: Browser = Browser(Config(driver=driver))

    browser.open(base_url)  # теперь base_url доступен и подставится из фикстуры

    yield browser  # Возвращаем browser в тест

    # Делаем аттачи
    attach.add_screenshot(browser)   # Аттач скриншота
    attach.add_html(browser)         # Аттач HTML-кода страницы
    attach.add_logs(browser)         # Аттач логов браузера
    attach.add_video(browser)        # Аттач видео (если поддерживается)

    # Закрываем браузер после выполнения теста
    browser.quit()