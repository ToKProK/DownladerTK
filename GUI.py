import flet as ft
from pars import parse_manga
from pars_ranob import parse_ranobe



def main_gui(page: ft.Page):
    page.title = "DownloaderTK"
    page.window_height = 500
    page.window_width = 900
    page.theme_mode = "dark"#light
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_height = 400
    page.window_min_width = 700
    
    # Получаем путь в котом создадим папку
    def pick_directory(e: ft.FilePickerResultEvent):
        if not e.path:
            dir_path.label = "None" # Если пользователь ничего не выбрал
        else:
            dir_path.label = e.path # Если пользователь выбрал путь
        page.update()


    def open_mangalib(e):
        page.launch_url('https://mangalib.me/')
    def open_ranobelib(e):
        page.launch_url('https://ranobelib.me/')

    def download_manga(e):
        but_start_manga.disabled = True # Отключаем кнопку
        url = url_manga_page.value
        page.update()
        parse_manga(link=url, path=dir_path.label)
        but_start_manga.disabled = False # Включаем кнопку, когда все скачалось
        page.update()

    def download_ranobe(e):
        but_start_ranobe.disabled = True # Отключаем кнопку
        url = url_ranobe_page.value
        page.update()
        parse_ranobe(link=url, path=dir_path.label)
        but_start_ranobe.disabled = False # Включаем кнопку, когда все скачалось
        page.update()
    img_ranobelib = ft.Container(width=100, height=100, image_src="icons/R_icon.png", on_click=open_ranobelib)
    img_mangalib = ft.Container(width=100, height=100, image_src="icons/M_icon.png", on_click=open_mangalib)
    but_start_manga = ft.OutlinedButton(text="Скачать", width=200, on_click=download_manga)# Кнопка скачать в разделе манги
    url_ranobe_page = ft.TextField(label="Введите url главной страницы", width=600)# Поле для ввода ссылки манги
    but_start_ranobe = ft.OutlinedButton(text="Скачать", width=200, on_click=download_ranobe)# Кнопка скачать в разделе ранобэ
    url_manga_page = ft.TextField(label="Введите url главной страницы", width=600)# Поле для ввода ссылки манги
    directory_label = ft.Text(value="Выберите папку сохранения")# Текст в разделе настройки
    dir_path = ft.TextField(label="None", width=600, disabled=True)# Поле где будет указан выбранный путь
    
    but_dir = ft.OutlinedButton(text="Выбрать папку",icon=ft.icons.FOLDER_COPY_OUTLINED, width=200, on_click=lambda _: directory.get_directory_path())# Кнопка выбора папки

    directory = ft.FilePicker(on_result=pick_directory)# Проводник
    page.overlay.append(directory)


    settings_page = ft.Row(
        [
            ft.Column(
                [
                    directory_label,
                    dir_path,
                    but_dir 
                ], 
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    manga_page = ft.Row(
        [
            ft.Column(
               [
                    ft.Text("MangaLib"),
                    img_mangalib,
                    url_manga_page,
                    but_start_manga
                    
               ],horizontal_alignment = ft.CrossAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    ranobe_page = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("RanobeLib"),
                    img_ranobelib,
                    url_ranobe_page,
                    but_start_ranobe
                ], horizontal_alignment = ft.CrossAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )



    def switch_page(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0:
            page.add(manga_page)
        elif index == 1:
            page.add(ranobe_page)
        elif index == 2:
            page.add(settings_page)
        page.update()
    

    page.navigation_bar = ft.NavigationBar(
        destinations=[
        ft.NavigationDestination(icon=ft.icons.CROP_ORIGINAL_SHARP, label="Mangalib"),
        ft.NavigationDestination(icon=ft.icons.AUTO_STORIES, label="Ranobelib"),
        ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ], on_change=switch_page
    )
    page.add(manga_page)
ft.app(target=main_gui)