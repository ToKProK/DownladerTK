from selenium import webdriver
import time, requests, img2pdf, os, shutil
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


my_list = []
path_list = []
count_chapters = 0
nomer_glavi = 1
title_name = ""
arthist = ""
time_pause = 2
def go_to_site(link):
    # try:
        global nomer_glavi
        nomer_glavi = 1
        #Настройка юзер агента
        user = UserAgent()
        user_now = user.random
        options = webdriver.ChromeOptions()
        #Делаем браузер невимым
        # options.add_argument("--headless=new")
        options.add_argument(f"user-agent={user_now}")
        #Получение драйвера и вставка юзер агента
        
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Firefox()
        #Растягиваем окно во всю ширину.
        driver.maximize_window()
        #Переход по ссылке
        driver.get(link)
        time.sleep(time_pause)

        #Попытка получить название
        title_name = driver.find_element(By.CLASS_NAME, "media-name__main").text

        #Нажимаю на кнопку начать читать
        driver.find_element(By.LINK_TEXT, "Начать читать").click()
        time.sleep(time_pause)
        #Кликаем по вкладке глав
        driver.find_element(By.XPATH, "//div[@data-reader-modal='chapters']").click()
        chapters = driver.find_elements(By.CLASS_NAME, "menu__item")
        count_chapters = (len(chapters))
        print(f"Количесвто глав = {count_chapters}")
        driver.find_element(By.CLASS_NAME, "popup_side").click()


        #Главы
        for i in range(0, count_chapters):
            #Смотрим количество страниц
            pages = driver.find_elements(By.XPATH, "//option")
            count_page = (len(pages))
            print(f"В данной главе {count_page} стр.")
            #Очищаем списки
            my_list.clear()
            path_list.clear()
            for b in range(1, count_page + 1):
                image = driver.find_element(By.XPATH, "//div[@class='reader-view__wrap']/img")
                img = image.get_attribute("src")
                print("Link + " + img)
                time.sleep(0.1)#если убрать эту паузу, то возникнет ошибка. Ссылка на решение проблемы - https://stackoverflow.com/questions/23557471/clicking-on-image-results-in-an-error-element-is-not-clickable-at-point-97-42
                image.click()
                time.sleep(0.2)

                my_list.append(img)

            headers = {
                "Accept": "*/*",
                "UserAgent":user_now
            }
            i = 0
            for img_url in my_list:

                req = requests.get(url=img_url, headers=headers)
                response = req.content
                i+=1
                with open(f"data/media/{i}.png", "wb") as file:
                    file.write(response)
                    path_list.append(f"data/media/{i}.png")
                    print(f"Download {i} page")
            print(f"Глава №{count_chapters} успешно скачана")
            #Конвертируем картинки в pdf файл.
            convert(title_name=title_name)
            #Удаляем все картинки
            Del_directory()
        print("Все главы скачанны")
        return True

    # except Exception as ex:
    #     print(ex)
    #     return False
    # finally:
    #     driver.close()
    #     driver.quit()


def convert(title_name):
    global nomer_glavi
    print(path_list)
    #Проверяем файл на наличие запрещённых символов
    title_name = Check_file_name(title_name)
    # Создаём пдф файл главы
    with open(f"data/pdf_files/{title_name}, {nomer_glavi}.pdf", "wb") as f:
        f.write(img2pdf.convert(path_list))
    print(f"Конвертация {nomer_glavi} главы прошла успешно!")
    nomer_glavi = nomer_glavi + 1

def Del_directory():
    folder = "data/media/"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
def Check_file_name(file_name):
    char_remov = ['*', '|', "\\", ':', '"', '<', '>', '?','/' ]
    for char in char_remov:
        file_name = file_name.replace(char, "#")
    return file_name

def main():
    link = "https://mangalib.me/nae-abeojiui-adeul-eul-chaj-aseo?section=info"
    go_to_site(link=link)

if __name__=="__main__":
    main()