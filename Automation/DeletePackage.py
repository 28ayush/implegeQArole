from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url= "https://ecs-qa.kloudship.com"
User= "kloudship.qa.automation@mailinator.com"
Pass= "Password1"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID, "login-email").send_keys(User)
driver.find_element(By.ID, "login-password").send_keys(Pass)
driver.find_element(By.ID, "login-btn").click()

mat_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-icon[text()="assessment" and @class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color"]'))
    )
mat_icon.click()

mat_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-icon[text()="delete" and @class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color"]'))
    )
time.sleep(3)
mat_icon.click()

span_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@class="mat-button-wrapper" and text()="Delete Package Type"]'))
    )
span_element.click()

mat_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-icon[text()="more_vert" and @class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color"]'))
    )
mat_icon.click()

mat_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-icon[text()="power_settings_new" and @class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color"]'))
    )
mat_icon.click()

print("successfully deleted")
