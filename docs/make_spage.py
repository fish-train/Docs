# coding : utf-8

import subprocess

# Сборка сайта
def make_spage():
	# Собрать сайт , перейти в папку сайта, запустить веб-сервер
    cmd = "make singlehtml & cd build/singlehtml & python -m http.server"
	# Выполнить команду CMD
    subprocess.Popen(cmd, shell = True)

make_spage() # Собрать сайт