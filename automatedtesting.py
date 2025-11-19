from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(url, username, password, expected_result):
    """
    Test login with valid/invalid credentials.
    
    Args:
        url: Login page URL
        username: Username to test
        password: Password to test
        expected_result: 'success' or 'failure'
    """
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        
        # Wait for and fill username field
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(username)
        
        # Fill password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        # Click login button
        login_button = driver.find_element(By.ID, "login_btn")
        login_button.click()
        
        # Check result
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "result"))
        )
        result_element = driver.find_element(By.CLASS_NAME, "result")
        actual_result = result_element.text
        
        return actual_result == expected_result
        
    finally:
        driver.close()

