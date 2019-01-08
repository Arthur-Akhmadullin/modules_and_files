import PyPDF2


with open("456.pdf", "rb") as f:
    pdf_content = PyPDF2.PdfFileReader(f)

    page = pdf_content.getPage(0)
    page_content = page.extractText()
    print(page_content.encode('utf-8').decode('unicode-escape').encode('latin1').decode('utf-8'))