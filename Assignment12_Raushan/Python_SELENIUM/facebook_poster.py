from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get('http://facebook.com')
emailelement = driver.find_element(By.XPATH,'.//*[@id="_r_4_"]')
emailelement.send_keys('raushan.engineer23@gmail.com')

passeleent = driver.find_element(By.XPATH,'.//*[@id="pass"]')
passeleent.send_keys('FRushan@123')

elem = driver.find_element(By.XPATH,'.//*[@id="loginbutton"]')
elem.click()

statuselement = driver.find_element(By.XPATH, "//*[@name='xhpc_message']")
time.sleep(5)

statuselement.send_keys('Hi there')
time.sleep(5)

buttons = driver.find_elements_by_tag_name('button')
time.sleep(5)

for button in buttons:
    if button.text == 'Post':
        button.click()

