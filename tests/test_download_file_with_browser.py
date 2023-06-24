import time
import os.path

from selenium import webdriver
from selene import browser
from conftest import TMP_DIR


options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": TMP_DIR,
    "download.prompt_for_download": False
}

options.add_experimental_option("prefs", prefs)

browser.config.driver_options = options


def test_download_file(tmp_dir_manager):

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(5)

    # Проверяем результаты
    assert os.path.exists(os.path.join(TMP_DIR, 'pytest-main.zip'))