from selenium import webdriver
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import json

#global variable
link=input(' input link shop :')
chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver =webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)

#open url lazada
driver.get (link)
sleep(4)

# use xpath
def driver_login(str):
        clickphone = driver.find_element_by_xpath(str)
        clickphone.click()
        sleep(random.randint(3,5))
        return clickphone
# use xpath
def dr_lg_list(str):
        click_phone2=driver.find_elements_by_xpath(str)
        sleep(random.randint(3,5))
        return click_phone2
# use class
def dr_lg_list_class(str):
        click=driver.find_elements_by_class_name(str)
        sleep(random.randint(3,5))
        return click

def close_window():
        driver.close()

def crawling(pth,name,amount,price,price_dis):     # 5 paramenters
        l=dr_lg_list(pth)
        f = open('data.txt', mode='a',encoding='utf-8')
        z='//'
        for element in l : 
                name_pd=element.find_element_by_class_name(name)
                number_of= element.find_element_by_class_name(amount)
                price_pd=element.find_element_by_xpath(price)
                price_dis_pd=element.find_element_by_xpath(price_dis)

                f.writelines(name_pd.text)
                f.writelines(number_of.text)
                f.writelines(price_pd.text)
                f.writelines(price_dis_pd.text)
                f.writelines(z)
                print('done')
        f.close()
             

if __name__ == '__main__':
        driver_login(str)
        dr_lg_list()
        close_window()
        crawling()
        dr_lg_list_class()


