from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# wait for email field
email = wait.until(
    EC.visibility_of_element_located((By.ID, "email"))
)

email.send_keys("raushan.engineer23@gmail.com")

# password
password = driver.find_element(By.ID, "pass")
password.send_keys("FRaushan@123")

# login
driver.find_element(By.NAME, "login").click()