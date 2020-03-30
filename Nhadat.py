import os
from selenium import webdriver
import time

chromedriver = "C:\Program Files\ChromeDriver\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh.html")

subwebs = driver.find_elements_by_class_name("ct_title")
subweblinks = list()
i  = 0
while i < len(subwebs):
    subweblinks.append(subwebs[i].find_element_by_css_selector('a').get_attribute('href'))
    i+=1
i = 0
for  x in subweblinks:
    driver.get(x)
    name = driver.find_element_by_class_name("name")
    phone = driver.find_element_by_class_name("fone")
    square =  driver.find_element_by_class_name("square")
    price =  driver.find_element_by_class_name("price")
    address =  driver.find_element_by_class_name("address")
    with open('Result.txt','a', encoding="utf-8") as f:
        f.write ('------------------------- New Node -------------------------\n')
        f.write(name.text + '\n')
        f.write(phone.text + '\n')
        f.write(square.text + '\n')
        f.write(price.text + '\n')
        f.write(address.text + '\n')
        f.write(x + '\n')
        f.write ('------------------------- End Node -------------------------\n\n\n')
    time.sleep(4)
print ('Finish..............')