import os
from datetime import datetime
import time
import json
import selenium
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
import re
import pdfkit
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PyPDF2 import PdfFileMerger, PdfFileReader
import winsound


def createConnection():
    URL = 'https://learning.oreilly.com/library/view/aspnet-core-in/9781617298301/OEBPS/Text/FM.htm'
    DRIVER = webdriver.Chrome('D:\Downloads\chromedriver_win32\chromedriver.exe')
    DRIVER.implicitly_wait(20)
    # Ждем 10 секунд, если не прогрузилось, возвращаем что сайт не работает
    DRIVER.set_page_load_timeout(20)
    try:
        return DRIVER
    except:
        return 0

def loadPage(URL):
    start_time = datetime.now()
    URL_log = 'https://www.oreilly.com/member/login/?next=%2Fapi%2Fv1%2Fauth%2Fopenid%2Fauthorize%2F%3Fclient_id%3D235442%26redirect_uri%3Dhttps%3A%2F%2Flearning.oreilly.com%2Fcomplete%2Funified%2F%26state%3DcLycNmp7UwvuA6eYoeiHRHr3Clg3ZVRn%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail&locale=en'
    pageDriver = createConnection()
    try:
        pageDriver.get(URL_log)
    except TimeoutException:
        return 0

    if (pageDriver != 0):

        input = pageDriver.find_element_by_class_name('orm-Input-root')
        if(type(input) != None):
            input = pageDriver.find_element_by_name('email')
            input.send_keys('login')
            pageDriver.find_element_by_name('password').click()
            time.sleep(3)
            pageDriver.find_element_by_class_name("orm-Button-btnContentWrap").click()

            input2 = pageDriver.find_element_by_name('login')
            input2.send_keys('login')
            input3 = pageDriver.find_element_by_name('password')
            input3.send_keys('password')
            pageDriver.find_element_by_class_name("button--light").click()
            time.sleep(2)

            pageDriver.get(URL)
            pageDriver.find_element_by_class_name('t-sign-in').click()
            input = pageDriver.find_element_by_name('email')
            input.send_keys('login')
            pageDriver.find_element_by_name('password').click()
            time.sleep(1)
            pageDriver.find_element_by_class_name("orm-Button-btnContentWrap").click()

            pageDriver.find_element_by_class_name('ss-list').click()
            # pages = pageDriver.find_elements_by_class_name("//li[@class='contains(text(), 'toc-level'']")
            pages = pageDriver.find_elements_by_xpath("//li[contains(@class, 'toc-level')]")
            pageDriver.find_element_by_class_name('close').click()

            name_of_book = pageDriver.find_element_by_xpath("//span[@class='sbo-title ss-list']")
            name_of_book_content = name_of_book.get_attribute('innerHTML')

            print(str(name_of_book_content).split('</div>')[1].replace("</h1>", ""))
            counter = 0
            print(len(pages))
            for page in range(len(pages)-1):
                if(counter==0):
                    pageDriver.find_element_by_class_name('next').click()
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'p')
                    time.sleep(2)
                    pyautogui.click(x=1100, y=210, clicks=1, button='left')
                    time.sleep(2)
                    pyautogui.click(x=1100, y=270, clicks=1, button='left')
                    time.sleep(5)
                    pyautogui.click(x=1100, y=890, clicks=1, button='left')
                    time.sleep(2)
                    pyautogui.write('Page' + '( ' + str(page) + ' ).pdf')
                    time.sleep(2)
                    pyautogui.click(x=800, y=570, clicks=1, button='left')
                else:
                    pageDriver.find_element_by_class_name('next').click()
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'p')
                    time.sleep(3)
                    pyautogui.click(x=1100, y=890, clicks=1, button='left')
                    time.sleep(2)
                    pyautogui.write('Page' + '( ' + str(page) + ' ).pdf')
                    time.sleep(2)
                    pyautogui.click(x=800, y=570, clicks=1, button='left')

                counter += 1

            mergedObject = PdfFileMerger()

            for fileNumber in range(len(pages)-1):
                mergedObject.append(PdfFileReader('D:\\Downloads\\Page'+'( '+str(fileNumber)+' ).pdf', 'rb'))
                os.remove('D:\\Downloads\\Page'+'( '+str(fileNumber)+' ).pdf')

            mergedObject.write('D:\\Desktop\\parsor\\output\\'+str(name_of_book_content).split('</div>')[1].replace("</h1>", "").replace("\n","").replace("\\n","").replace("  ", "").replace(":", " ")+'.pdf')

        else:
            # Возвращаем код 1 - ничего не найдено
            return 1
    else:
        # Возвращаем код 0 - сайт недоступен
        return 0

    print(datetime.now() - start_time)
    print('\a')
    winsound.Beep(440, 500)


if __name__ == '__main__':
    with open("D:\\Desktop\\parsor\\input\\inp.txt") as file:
        array = [row.strip() for row in file]
    count = 0
    for page in array:
        print(page)
        loadPage(page)






