# coding : utf-8

import subprocess

# Сборка сайта
def make_site():
    # Собрать сайт , перейти в папку сайта, запустить веб-сервер
    cmd = "make html & cd build/html & python -m http.server"
    # Выполнить команду CMD
    subprocess.Popen(cmd, shell = True)

make_site()	# Собрать сайт