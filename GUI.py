import flet as ft
from pars import parse_manga

def main_gui(page: ft.Page):
    page.title = "DownloaderTK"
    page.theme_mode = "dark"#light
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_height = 300
    page.window_min_width = 700
    url_manga_page = ft.TextField(label="Введите url главной страницы", width=600)


    def download_manga(e):
        but_start_manga.disabled = True
        url = url_manga_page.value
        parse_manga(link=url)
        page.update()
    but_start_manga = ft.OutlinedButton(text="Скачать", width=200, on_click=download_manga)

    url_ranobe_page = ft.TextField(label="Введите url главной страницы", width=600)
    but_start_ranobe = ft.OutlinedButton(text="Скачать", width=200)



    manga_page = ft.Row(
        [
            ft.Column(
               [
                    ft.Text("MangaLib"),
                    url_manga_page,
                    but_start_manga,
                    
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
        page.update()
    

    page.navigation_bar = ft.NavigationBar(
        destinations=[
        ft.NavigationDestination(icon=ft.icons.CROP_ORIGINAL_SHARP, label="Mangalib"),
        ft.NavigationDestination(icon=ft.icons.AUTO_STORIES, label="Ranobelib")
        ], on_change=switch_page
    )
    page.add(manga_page)
ft.app(target=main_gui)