import csv
import os

# Задаем уникальный путь до CSV файла
csv_file= os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../resources/eggs.csv')
)


def test_create_csv_file():

    # Формируем CSV файл и записываем в него данные
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    # Проверяем результаты
    assert os.path.exists(csv_file)


# Читаем CSV файл и проверяем данные
def test_read_csv_file():
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:

            # Проверяем результаты
            assert len(row) == 3

            # Проверяем результаты
    assert csvreader.line_num == 2

    # Удаляем сформированный CSV файл
    os.remove(csv_file)
