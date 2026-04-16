from selenium import webdriver
import numpy as np
import time

path_webdriver = 'D:/Comunidade DS/Portifólio de Projetos/repos/ds_ab_baysian/driver/chromedriver.exe'
driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8001/home')

clicks = 10000
for click in range (clicks):
    if np.random.random() < 0.4:
        driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()
        time.sleep(0.5)
    else:
        driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()
        time.sleep(0.5)