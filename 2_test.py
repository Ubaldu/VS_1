import pytest
from selenium.webdriver import Chrome
from verify import *

import allure
from allure_commons.types import AttachmentType

@pytest.fixture
def chrome_2():
    print('Run before test')
    driver = Chrome()
    yield driver
    driver.quit()
    print('Run after test') 

def test_start_1(chrome_2):
    chrome_2.maximize_window()
    chrome_2.get("https://the-internet.herokuapp.com/login")

    expect(chrome_2.title).to_be_equal('The Internet')

def test_start_2(Chrome):
    Chrome.maximize_window()
    Chrome.get("https://the-internet.herokuapp.com/login")
    

    expect(chrome_2.title).to_be_equal("https://the-internet.herokuapp.com/login")