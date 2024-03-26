from GUI import main_gui
import flet as ft
def main():
    ft.app(
        target=main_gui,
        assets_dir="assets"
        )

if __name__=="__main__":
    main()

#flet pack main.py --icon "icon.png" --add-data "assets:assets" - Упаковка приложения
#https://flet.dev/docs/guides/python/packaging-desktop-app/