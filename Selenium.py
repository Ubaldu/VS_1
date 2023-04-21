# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from time import sleep
# from selenium.webdriver.common.keys import Keys

# def diff_text(actual_result, expected_result):
#     if actual_result == expected_result:
#         print(f'{actual_result} равно {expected_result}')
#         print("Тест пройден")
#     else:
#         print(f'{actual_result} не равно {expected_result}')
#         print("Ошибка!")
    
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/login")
# username_box = driver.find_element(by=By.NAME, value="username")
# username_box.clear()
# username_box.send_keys("tomsmith")
# # sleep(1)
# password_box = driver.find_element(by=By.NAME, value="password")
# password_box.clear()
# password_box.send_keys("SuperSecretPassword!")

# login_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# login_button.click()
# current_url = driver.current_url

# welcome_messsage = driver.find_element(by=By.CLASS_NAME, value="subheader")
# welcome_text = welcome_messsage.text

# label = driver.find_element(by=By.CSS_SELECTOR, value=".example h2")
# label_text = label.text

# green_label = driver.find_element(by=By.CSS_SELECTOR, value="#flash")
# green_text = green_label.text
# green_text_replace = green_text.replace("×", "")
# green_text_strip_final = green_text_replace.strip()

# logout_button = driver.find_element(by=By.CSS_SELECTOR, value='[href="/logout"]')
# logout_button.click()

# # driver.maximize_window()

# driver.refresh()

# links = driver.find_elements(by=By.CSS_SELECTOR, value='#flash')

# assert len(links) == 0


# diff_text(green_text_strip_final, "You logged into a secure area!")
# diff_text(current_url, "https://the-internet.herokuapp.com/secure")
# diff_text(welcome_text, "Welcome to the Secure Area. When you are done click logout below.")
# diff_text(label_text, "Secure Area")

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/checkboxes")

# checkbox1 = driver.find_element(by=By.CSS_SELECTOR, value='#checkboxes > input:nth-child(1)')
# checkbox1.click()

# checkbox2 = driver.find_element(by=By.CSS_SELECTOR, value='#checkboxes > input:nth-child(3)')
# checkbox2.click()

# assert checkbox1.get_attribute('checked') == 'true'
# assert checkbox2.get_attribute('checked') == None

# sleep(5)

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select

# driver = webdriver.Firefox()
# driver.get("http://shpargalkablog.ru/2016/08/select-options.html")

# select_element = driver.find_element(by=By.CSS_SELECTOR, value='#post-body-1902682558794375045 > select:nth-child(56)')
# select = Select(select_element)
# # select.select_by_value("Cucumis melo")
# print(select.first_selected_option.text)

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
# add_element = driver.find_element(by=By.CSS_SELECTOR, value='.example > button:nth-child(1)')

# add_count = 10
# del_count = 5
# expected_result = add_count - del_count

# for i in range(add_count):
#     add_element.click()

# del_button = driver.find_elements(by=By.CSS_SELECTOR, value='button.added-manually')

# for i in range(del_count):
#     del_button[i].click()

# del_button = driver.find_elements(by=By.CSS_SELECTOR, value='button.added-manually')

# assert len(del_button) == expected_result

# sleep(10)

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select

# driver = webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# js_alert_button = driver.find_element(by=By.CSS_SELECTOR, value='.example > ul:nth-child(3) > li:nth-child(1) > button:nth-child(1)')
# js_alert_button.click()

# alert = driver.switch_to.alert
# sleep(2)
# alert.accept()
# input_text = "12345"

# prompt_button = driver.find_element(by=By.CSS_SELECTOR, value='.example > ul:nth-child(3) > li:nth-child(3) > button:nth-child(1)')
# prompt_button.click()
# prompt = driver.switch_to.alert
# prompt.send_keys(input_text)
# sleep(2)
# prompt.dismiss()

# result = driver.find_element(by=By.CSS_SELECTOR, value='#result')

# assert not(input_text in result.text)
# driver.quit()

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select

# driver = webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/windows")

# main_window = driver.window_handles
# print(main_window)
# link = driver.find_element(by=By.LINK_TEXT, value='Click Here')
# link.click()
# windows_arr = driver.window_handles
# print(windows_arr)
# for i in windows_arr:
#     if i != main_window[0]:
#         driver.switch_to.window(i)
# sleep(2)
# label = driver.find_element(by=By.TAG_NAME, value='h3')
# print(driver.current_window_handle)
# print(label.text)

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains

# def alert_is_present():
#     try:
#         driver.switch_to.alert
#         return True
#     except:
#         return False

# driver = webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/context_menu")
# box = driver.find_element(by=By.ID, value='hot-spot')
# actions = ActionChains(driver)
# actions.context_click(box).perform()

# assert alert_is_present() == True

# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains

#  from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# add_element = driver.find_element(by=By.CSS_SELECTOR, value='.example > button:nth-child(1)')

# for i in range(5):
#     add_element.click()
            
# for i in range(4):            
#     del_button = driver.find_element(by=By.CSS_SELECTOR, value='button.added-manually')
#     del_button.click()
    
# ==========================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/challenging_dom")

# del_button = driver.find_element(by=By.XPATH, value='./html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a[2]')

# del_button.click()

# ==========================================================================================================================


# class Calculator:
    
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
#     def add(self):
#         return self.a + self.b
    
#     def substruct(self):
#         return self.a - self.b
    
#     def multiplly(self):
#         return self.a * self.b
    
#     def divide(self):
#         return self.a / self.b
    
# import unittest

# class CalculatorTest(unittest.TestCase):
    
#     def setUp(self) -> None:
#         print("Создаю объект калькулятора")
#         self.calc = Calculator(6, 3)
    
#     def test_add(self):
#         expected = 9
#         actual = self.calc.add()
#         self.assertEqual(expected, actual, 'должно быть 9')
        
#     def test_substruct(self):
#         expected = 3
#         actual = self.calc.substruct()
#         self.assertEqual(expected, actual, 'должно быть 3')
        
#     def test_multiply(self):
#         expected = 18
#         actual = self.calc.multiplly()
#         self.assertEqual(expected, actual, 'должно быть 18')
        
#     def test_divide(self):
#         expected = 2
#         actual = self.calc.divide()
#         self.assertEqual(expected, actual, 'должно быть 2')
        
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

#==========================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import unittest

# class LoginTest(unittest.TestCase):
    
#     def setUp(self) -> None:
#         return super().setUp()
    
#     def tearDown(self) -> None:
#         return super().tearDown()
    
#     def test_success_login(self):
#         driver = webdriver.Chrome()
#         driver.get("https://the-internet.herokuapp.com/login")
#         login_input = driver.find_element(By.XPATH, '//*[@id="username"]')
#         password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
#         login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i')
#         login_input.send_keys("tomsmith")
#         password_input.send_keys("SuperSecretPassword!")
#         login_button.click()
        
#         self.assertIn("/secure", driver.current_url)
#         driver.quit()
        
#     def test_fail_login(self):
#         driver = webdriver.Chrome()
#         driver.get("https://the-internet.herokuapp.com/login")
#         login_input = driver.find_element(By.XPATH, '//*[@id="username"]')
#         password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
#         login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i')
#         login_input.send_keys("tomsmithFail")
#         password_input.send_keys("SuperSecretPassword!")
#         login_button.click()
        
#         fail_message = driver.find_element(By.XPATH, '//*[@id="flash"]')
#         self.assertIn("Your username is invalid!", fail_message.text)
#         driver.quit()
        
#     def test_fail_password(self):
#         driver = webdriver.Chrome()
#         driver.get("https://the-internet.herokuapp.com/login")
#         login_input = driver.find_element(By.XPATH, '//*[@id="username"]')
#         password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
#         login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i')
#         login_input.send_keys("tomsmith")
#         password_input.send_keys("SuperSecretPassword!fail")
#         login_button.click()
        
        
#         fail_message = driver.find_element(By.XPATH, '//*[@id="flash"]')
#         self.assertIn("Your password is invalid!", fail_message.text)
#         driver.quit()
        
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
    
#==================================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import unittest

# class AddRemuveTest(unittest.TestCase):
    
#     def setUp(self) -> None:
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    
#     def tearDown(self) -> None:
#         self.driver.quit()
    
# # 1. Проверим, отображается ли на странице надпись Add/Remove Elements и
# # есть ли кнопка Add element
    
#     def test_succes_add_remove_elements(self):
#         add_remove_string = self.driver.find_element(By.CSS_SELECTOR, '#content > h3:nth-child(1)')
#         add_rem_string_text = add_remove_string.text

#         add_element = self.driver.find_element(by=By.CSS_SELECTOR, value='.example > button')
        
#         self.assertIn("Add/Remove Elements", add_rem_string_text)
#         self.assertTrue(add_element.is_displayed())
        
# # 2. Проверим, работает ли кнопка Add Element, нажмем на нее три раза, ожидаемый результат - должнны 
# # появиться три кнопки Delete

#     def test_add_element(self):
#         add_element = self.driver.find_element(by=By.CSS_SELECTOR, value='.example > button')
#         for i in range(3):
#             add_element.click()

#         del_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.added-manually')
        
#         self.assertEqual(len(del_buttons), 3)

# # 3. Проверим, работает ли кнопка Delete, добавим три кнопки Delete и удалим две из них

#     def test_delete_assert(self):
#         add_element = self.driver.find_element(by=By.CSS_SELECTOR, value='.example > button')
#         for i in range(3):
#             add_element.click()
            

#         del_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.added-manually')
#         for i in range(2):
#             del_buttons[i].click()
            
    
#         del_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.added-manually')
        
#         self.assertEqual(len(del_buttons), 1)
               
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

#==============================================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.action_chains import ActionChains
# import unittest


# class DynamicLoadedElements(unittest.TestCase):
    
#     url = 'https://the-internet.herokuapp.com/dynamic_loading/1'
    
#     def test_dynamic_loaded(self):
#         driver = webdriver.Chrome()
#         wait = WebDriverWait(driver, 10)
#         driver.get(self.url)
#         driver.find_element(By.CSS_SELECTOR, '#start > button:nth-child(1)').click()
#         wait.until(expected_conditions.visibility_of_element_located(By.CSS_SELECTOR, '#finish > h4:nth-child(1)'))
        
#         finish_text = (wait.until(expected_conditions.visibility_of_element_located(By.CSS_SELECTOR, '#finish > h4:nth-child(1)'))).text
        
#         self.assertEqual(finish_text, 'Hello World!')
#         # driver.quit()  
        
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

#=======================================================================================================================

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import unittest

# class SiteTesting(unittest.TestCase):
    
#     def setUp(self) -> None:
#         o = Options()
#         o.add_experimental_option("detach", True)
#         self.driver = webdriver.Chrome(options=o)
#         self.driver.get("https://www.nix.ru/")
        
    
#     def tearDown(self) -> None:
#         pass

#     def test_load(self):
#         current_url = self.driver.current_url
#         self.assertEqual(current_url, 'https://www.nix.ru/')


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
    
#=====================================================================================================

# import requests
# from requests.exceptions import HTTPError
 
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
 
#         # если ответ успешен, исключения задействованы не будут
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')