from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click Electronics section
electronics = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Electronics"))
)
electronics.click()

# Click Mobiles
mobiles = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Mobiles"))
)
mobiles.click()