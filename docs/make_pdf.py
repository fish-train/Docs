# coding : utf-8

import subprocess
from docx2pdf import convert

# Сборка DOCX
def make_docx():
    # Собрать DOCX
    cmd = "make docx"
    # Выполнить команду CMD
    subprocess.Popen(cmd, shell = True)

# Конвертация DOCX в PDF
def make_pdf():
    # Конвертировать DOCX в PDF
    convert("build/docx/sphinx-test.docx")

make_docx() # Собрать DOCX
make_pdf()	# Конвертировать DOCX в PDF