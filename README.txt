Данное приложение скачивает мангу и ранобэ с сайтов: https://mangalib.me/ и https://ranobelib.me/.
Приложение кроссплатформенное, поэтому запуститься как на Windows, так и на Linux.
Инструкция запуска
1) Скачайте пайтион
2) в папке с проектом установите все зависимости, через файл "requirements.txt" выполнив команду "pip install -r requirements.txt"
3) Запустить выполнение кода
Билд приложения
После успешного запуска приложения можно следать его билд, для этого нужно выполнить следующие команды:
1) pip install PyInstaller
2) flet pack main.py --icon "down.png" --add-data "assets:assets"
Если возникли тружности ссылка на билд приложения на flet - "https://flet.dev/docs/cookbook/packaging-desktop-app/"