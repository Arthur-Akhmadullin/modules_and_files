from docx import Document

def word_edit(word, s1, s2):
    document = Document(word)

    for par in document.paragraphs:
        if s1 in par.text:
            par.text = s2

    document.save("документ_копия.docx")


string_1 = "С печальным шумом обнажалась,"
string_2 = "Когда я на почте служил ямщиком"

with open('документ.docx', 'rb') as f:
    word_edit(f, string_1, string_2)