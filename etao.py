# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import macNotify
import datetime
import sys

def doCheckIn(account, pwd):
	frame = driver.find_element_by_tag_name("iframe")
	driver.get(frame.get_attribute("src"))
	inputElement = driver.find_element_by_css_selector("label[for='J_SafeLoginCheck']")
	inputElement.click()
	print account + ":" + inputElement.get_attribute("value")

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
driver.get("http://login.etao.com/?logintype=taobao")
checkByCode()
# driver.quit()
