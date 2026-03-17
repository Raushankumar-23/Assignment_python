from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

driver.maximize_window()

driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphones")

driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

list = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")

# products found
print(str(list))

for i in list:

    print(i.list)

driver.quit()