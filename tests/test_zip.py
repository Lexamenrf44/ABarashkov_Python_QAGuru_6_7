import os
import zipfile

from conftest import TMP_DIR

# Переменные
# Задаем уникальный путь
resources_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))

# Задаем файлы
resources_files = os.listdir(resources_directory)

# Задаем архив
archive = os.path.join(TMP_DIR, 'test.zip')


def test_created_zip_file(tmp_dir_manager):
    with zipfile.ZipFile(archive, mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in resources_files:
            add_file = os.path.join(resources_directory, file)
            zf.write(add_file, arcname=file)

    with zipfile.ZipFile(archive) as zf:

        # Проверяем результаты
        assert len(resources_files) == len(zf.infolist())

        for file in resources_files:
            info = zf.getinfo(file)

            # Проверяем результаты
            assert file == info.filename
            orig_file_size = os.stat(os.path.join(resources_directory, file)).st_size

            # Проверяем результаты
            assert orig_file_size == info.file_size
