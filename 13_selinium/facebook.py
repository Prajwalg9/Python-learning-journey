from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize Firefox driver
driver = webdriver.Firefox()

try:
    # Navigate to demo login page (adapt for Facebook/travelocity)
    driver.get("https://demoqa.com/login")

    # Wait for and fill email field
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userEmail"))
    )
    email.send_keys("demouser@test.com")  # Replace with test credentials [file:12]

    # Wait for and fill password field
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userPassword"))
    )
    password.send_keys("demopass123")  # Replace with test credentials [file:13]

    # Wait for and click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login"))
    )
    login_button.click()

    # Wait for status message (success/error check)
    status = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))  # Or error span
    )
    print("Status message:", status.text)  # Verify login [web:21]

    time.sleep(2)  # Brief pause for observation only

except TimeoutException:
    print("Element not found or page load timeout")
finally:
    driver.quit()
