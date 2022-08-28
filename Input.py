import time
import requests
from htmldom import htmldom
from selenium import webdriver
import random

from selenium.webdriver.common.by import By
#https://spark.ru/auth
#https://dobro.ru/register
browser = webdriver.Chrome()
global param
def text():
    browser.get("")
    browser.maximize_window()
    a = browser.find_elements(By.XPATH, "//input[@type='text']")
    words = [ "1", "2", "3", "4"]

    c = 0
    #words=(random.choice(wordsrus[c]))
    for i in a:
        if i.get_attribute('value') == '':
            i.send_keys(words[c])
            c = c + 1
        else:
            continue

def password():
    b = browser.find_elements(By.XPATH, "//input[@type='password']")
    for i in b:
        i.send_keys("CwIk972!")



def emails():
    c = browser.find_elements(By.XPATH, "//input[@type='email']")
    for i in c:
        i.send_keys("testmachine@mail.ru")


def numbers():
    e = browser.find_elements(By.XPATH, "//input[@type='phone']")
    for i in e:
        i.click()
        i.send_keys("889998989898")


def checkboxes():
    f = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
    for i in f:
        i.click()










if __name__ == '__main__':
    text()
    password()
    emails()
    numbers()
    time.sleep(4)
    checkboxes()
