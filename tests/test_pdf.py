import os.path

from pypdf import PdfReader
from path import dir_res


def test_pdf():
    pdf_file = os.path.join(dir_res, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    # Проверяем результаты
    assert 412 == number_of_pages
