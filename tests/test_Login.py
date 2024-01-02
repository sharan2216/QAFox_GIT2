import time
from selenium import webdriver
from selenium.webdriver.common.by import By

//branch one changes
//new comments added here
def test_login_with_valid_credentials():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(2)
    driver.find_element(By.ID,"input-email").send_keys("sksharan666@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "input-password").send_keys("155113412")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(2)
    actual_text=driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text
    expected_text="Edit your account information"
    assert actual_text.__eq__(expected_text)
    driver.quit()


