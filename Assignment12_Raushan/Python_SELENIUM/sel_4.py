from selenium import webdriver
import time

driver = webdriver.Chrome()   # Correct (C must be capital)

driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(5)

driver.refresh()