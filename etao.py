from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

import os, re

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

driver.get("http://login.etao.com")

# find the element that's name attribute is q (the google search box)
driver.switch_to_frame(0)
element = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, "TPL_username_1")))

pwd = os.path.split(os.path.realpath(__file__))[0]
username = ''
password = ''
with open(os.path.join(pwd, './etao.code.txt')) as auth_txt:
    auth_code = auth_txt.read().strip().split(' ')
    username, password = auth_code[0], auth_code[1]

element.send_keys(username)
driver.find_element_by_id("TPL_password_1").send_keys(password)
driver.find_element_by_id("J_SubmitStatic").click()
element = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "ci_receive")))
print element.text
element.click()
driver.quit()