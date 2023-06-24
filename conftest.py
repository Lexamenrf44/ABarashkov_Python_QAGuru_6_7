import os
import glob
import pytest


TMP_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../tmp')
)


@pytest.fixture(scope='function', autouse=False)
def tmp_dir_manager():
    """
    Создаёт директорию для скачанных файлов и удаляет их после выполнения теста,
    чтобы при каждом запуске теста можно было удостовериться, что файл скачан.
    Из-за быстрого удаления файлов Chrome выдаёт ошибку "Не удалось скачать"
    после загрузки файла, на выполнение теста она не влияет.
    """
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)

    yield

    files = glob.glob(os.path.join(TMP_DIR, '*'))
    for f in files:
        os.remove(f)