import selenium
from tools import *;
import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys


#global variable:
class_pd='shop-search-result-view__item col-xs-2-4'
all_el_pd="//div[@class='shop-search-result-view__item col-xs-2-4']"     
classname_pd='ZG__4J'
classcount_sold='_1uq9fs'
classprice='//div[@class="zp9xm9 U-y_Gd _3rcqcF"]'
classprice_discount='//div[@class="zp9xm9 kNGSLn l-u0xK"]'
button_next='//button[@class="shopee-icon-button shopee-icon-button--right "]'

# crawling name shop 
class_name_shop='shopee-seller-portrait__name'
n=driver.find_element_by_class_name(class_name_shop)
f = open('data.txt', mode='a',encoding='utf-8')
f.writelines(n.text)
f.close()
print(n.text)

#crawling product data
pages=driver.find_elements_by_class_name('shopee-button-no-outline')
crawling(all_el_pd,classname_pd,classcount_sold,classprice,classprice_discount)

for data in pages :
    crawling(all_el_pd,classname_pd,classcount_sold,classprice,classprice_discount)
    driver_login(button_next)
close_window()













