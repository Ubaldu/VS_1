from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class LoginTest(unittest.TestCase):
    
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_success_login(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        login_input = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i')
        login_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")
        login_button.click()
        
        self.assertIn("/secure", driver.current_url)
        driver.quit()
        
    def test_fail_login(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        login_input = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i')
        login_input.send_keys("tomsmithFail")
        password_input.send_keys("SuperSecretPassword!")
        login_button.click()
        
        fail_message = driver.find_element(By.XPATH, '//*[@id="flash"]')
        self.assertIn("Your username is invalid!", fail_message.text)
        driver.quit()
        
    def test_fail_password(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        login_input = driver.find_element(By.XPATH, '//*[@id="username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i')
        login_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!fail")
        login_button.click()
         
        fail_message = driver.find_element(By.XPATH, '//*[@id="flash"]')
        self.assertIn("Your password is invalid!", fail_message.text)
        driver.quit()

    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)