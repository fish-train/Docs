# coding : utf-8

import subprocess

# Сборка сайта
def make_site():
	cmd = "make html & cd build/html & python -m http.server"		# Собрать сайт , перейти в папку сайта, запустить веб-сервер
	subprocess.Popen(cmd, shell = True)									    # Выполнить команду CMD

make_site()																	# Собрать сайт
