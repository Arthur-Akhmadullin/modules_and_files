import PyPDF2


with open("123.pdf", "rb") as f:
    pdf_content = PyPDF2.PdfFileReader(f)

    page = pdf_content.getPage(14)
    page_content = page.extractText()
    print(page_content.encode('utf-8'))