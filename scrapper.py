from selenium import webdriver
import time
import csv
import pandas as pd

def scrape(url):
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(5)

    for i in range(1,30):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

    name = driver.find_elements_by_class_name('_3ENhq')
    price = driver.find_elements_by_class_name('_6KkG6')
    details = driver.find_elements_by_class_name('_Ecri')

    with open(f'dump/results.csv','a') as f:
        for i in range(len(name)):
            f.write(name[i].text + "," + details[i].text.replace(",","") + "," + price[i].text.replace(",","") + "," + url + "\n")
    driver.close()
