import os.path

from pypdf import PdfReader


def test_pdf():
    reader = PdfReader(os.path.abspath('../resources/docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    # Проверяем результаты
    assert 412 == number_of_pages
