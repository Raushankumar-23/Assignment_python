from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")
time.sleep(5)

button = driver.find_element(By.NAME, "btnK")
button.click()

time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

driver.quit()