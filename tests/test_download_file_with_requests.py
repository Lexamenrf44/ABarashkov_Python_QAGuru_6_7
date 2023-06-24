import os
import requests

from conftest import TMP_DIR

# Variables settings out of test
url = 'https://selenium.dev/images/selenium_logo_square_green.png'
path_to_file = os.path.abspath(os.path.join(TMP_DIR, 'selenium_logo.png'))


def test_download_file_with_requests(tmp_dir_manager):
    response = requests.get(url)

    # Проверяем результаты
    assert response.status_code == 200

    with open('selenium_logo.png', 'wb') as file:
        file.write(response.content)

    size = os.path.getsize('selenium_logo.png')

    # Проверяем результаты
    assert 30803 == size
