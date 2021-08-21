from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import winsound
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()

#add path to chrome user profile data directory
options.add_argument(r"user-data-dir=C:\Users\piyus\AppData\Local\Google\Chrome\User Data\Default")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH, options=options)


#you can replace link0 and link1 with links for any two categories of contests
link0 = "https://www.dream11.com/football/contests/A%20League%202020-21/1663/29493?sectionIds[]=14"
link1 = "https://www.dream11.com/football/contests/A%20League%202020-21/1663/29493?sectionIds[]=15"
current = 0
while 1:
    if current:
        driver.get(link1)
        current = 0
    else:
        driver.get(link0)
        current = 1
    sleep(3)

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    page_source = BeautifulSoup(html, features='lxml')
    contest_links = page_source.find_all('a', "js--contest-card contestCardWrapper_fbec5 containerShadow_c2514")

    for link in contest_links:
        contest_link = "https://www.dream11.com" + str(link.get('href').replace(" ", "%20"))
        # print(contest_link)
        driver.get(contest_link)
        sleep(3)
        driver.find_element_by_class_name('tabItemInactive_06be2.tabItem_8556a').click()
        sleep(3)
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        page_source = BeautifulSoup(html, features='lxml')
        player_names = driver.find_elements_by_class_name("playerUserName_1ac16")
        for name in player_names:
            # replace "Ronaldo 88" with any other username whom you wish to search
            if str(name.text) == "Ronaldo 88":
                print("found Ronaldo 88")
                winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
                print(contest_link)

driver.quit()
