from selenium import webdriver
import numpy as np
import time

path_webdriver = 'D:/Comunidade DS/Portifólio de Projetos/repos/ds_ab_baysian/driver/chromedriver.exe'
driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8001/home')

clicks = 10000
for click in range (clicks):
    button_color = driver.find_element('name', 'yescheckbox').get_attribute('value')

    


    if button_color == 'blue':
        if np.random.random() < 0.30:
            driver.find_element('name', 'yescheckbox').click()
            driver.find_element('id', 'yesbtn').click()
        else:
            driver.find_element('name', 'nocheckbox').click()
            driver.find_element('id', 'nobtn').click()
    else:
        if np.random.random() < 0.35:
            driver.find_element('name', 'yescheckbox').click()
            driver.find_element('id', 'yesbtn').click()
        else:
            driver.find_element('name', 'nocheckbox').click()
            driver.find_element('id', 'nobtn').click()

    time.sleep(0.4)