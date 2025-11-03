import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_empty_fields(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "All fields are required."
    alert.accept()

def test_invalid_email(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "email").send_keys("invalidemail")
    driver.find_element(By.NAME, "password").send_keys("abcdef")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Enter a valid email address."
    alert.accept()

def test_short_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Password must be at least 6 characters long."
    alert.accept()

def test_successful_login_and_pin_navigation(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("abcdef")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(2)
    assert "/home" in driver.current_url
    first_pin = driver.find_elements(By.CLASS_NAME, "pin")[0]
    first_pin.click()
    time.sleep(2)
    assert "Back to Home" in driver.page_source
