# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import macNotify
import datetime
import sys

def doCheckIn(account, pwd):
	driver.delete_all_cookies()
	driver.get("http://login.etao.com/?logintype=taobao")
	frame = driver.find_element_by_tag_name("iframe")
	driver.get(frame.get_attribute("src"))
	driver.implicitly_wait(3)
	#inputElement = driver.find_element_by_css_selector("label[for='J_SafeLoginCheck']")
	#inputElement.click()
	inputElement = driver.find_element_by_id("J_SafeLoginCheck")
	if inputElement.get_attribute("value") == "on":
		print inputElement.get_attribute("value")
		inputElement.click()
	print datetime.datetime.now()
	#print inputElement.get_attribute("value")
	inputElement = driver.find_element_by_id("TPL_username_1")
	inputElement.send_keys(account)
	inputElement = driver.find_element_by_id("TPL_password_1")
	inputElement.send_keys(pwd)
	inputElement = driver.find_element_by_id("J_SubmitStatic")
	inputElement.click()
	#print account + ":" + inputElement.get_attribute("value")

def signClick():
	driver.get("http://www.etao.com")
	inputElement = driver.find_element_by_css_selector(".ci_receive")
	inputElement.click()
	print inputElement.text

	driver.get("http://taojinbi.taobao.com/index.htm")
	inputElement = driver.find_element_by_css_selector(".J_GoTodayBtn")
	inputElement.click()
	print inputElement.text

def logError(message, e):
	print message
	print e
	with open('error.code.txt', 'a') as errorTxt:
		errorTxt.write(str(datetime.datetime.now()))
		errorTxt.write(message)
		errorTxt.write(str(e))
		errorTxt.write('\n')

def checkIn(account, pwd):
	try:
		doCheckIn(account, pwd)
		signClick()
		pass
	except Exception, e:
		logError('etao checkIn failure', e)
		macNotify.notify("etao checkIn failure", account, str(e))
		pass
	else:
		pass
	finally:
		pass

def checkByCode():
	with open('etao.code.txt') as codeTxt:
	    for line in codeTxt:
	        nos = line.rstrip().split(' ')
	        account, pwd = nos[0], nos[1]
	        checkIn(account, pwd)

reload(sys) 
sys.setdefaultencoding('utf8')
driver = webdriver.Firefox()
checkByCode()
#driver.quit()
