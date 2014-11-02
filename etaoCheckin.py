# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import macNotify
import datetime
import time
import sys

def doCheckIn(driver, account, pwd):
	driver.delete_all_cookies()
	driver.get("http://login.etao.com/?logintype=taobao")
	frame = driver.find_element_by_tag_name("iframe")
	driver.get(frame.get_attribute("src"))
	#inputElement = driver.find_element_by_css_selector("label[for='J_SafeLoginCheck']")
	#inputElement.click()
	#inputElement = driver.find_element_by_css_selector("input[id=J_SafeLoginCheck]")
	#print inputElement.get_attribute("value") + str(datetime.datetime.now())
	#if inputElement.get_attribute("value") == "on":
	#	inputElement.click()
	#inputElement = driver.find_element_by_css_selector("#J_PasswordEdit object embed")

	inputElement = driver.find_element_by_id("TPL_username_1")
	inputElement.send_keys('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
	inputElement.send_keys(account)
	inputElement = driver.find_element_by_id("TPL_password_1")
	inputElement.send_keys(pwd)
	inputElement = driver.find_element_by_id("J_SubmitStatic")
	inputElement.click()
	#print account + ":" + inputElement.get_attribute("value")

def appendRandom(prefix):
	return prefix + "random_dt=" + datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S%f")

def sendTaoJinBiCode(driver):
	try:
		inputElement = driver.find_element_by_css_selector(".J_CoinCheckCode")
		input_seccode=unicode(raw_input('enter:'))
		pass
	except Exception, e:
		print 'no sendTaoJinBiCode'
		pass
	else:
		inputElement.send_keys(input_seccode)
		driver.find_element_by_css_selector(".J_SubmitCodeBtn").click()
		pass
	finally:
		pass

def signClick(driver):
	driver.get("http://www.etao.com")
	inputElement = driver.find_element_by_css_selector(".ci_receive")
	inputElement.click()
	print "etao:" + inputElement.text

	driver.get("http://vip.tmall.com/?signIn=true")
	inputElement = driver.find_element_by_css_selector(".J_LotteryBtn")
	inputElement.click()
	print "vip.tmall:" + inputElement.text

	driver.get("http://taojinbi.taobao.com/index.htm")
	inputElement = driver.find_element_by_css_selector(".J_GoTodayBtn")
	print "taojinbi:" + inputElement.text
	inputElement.click()
	sendTaoJinBiCode(driver)

	driver.get("http://ka.tmall.com")
	time.sleep(2)
	inputElement = driver.find_element_by_id("signTrigger")
	inputElement.click()
	print "ka.tmail:" + inputElement.get_attribute("title")

def logError(message, e):
	print message
	print e
	with open('error.code.txt', 'a') as errorTxt:
		errorTxt.write(str(datetime.datetime.now()))
		errorTxt.write(message)
		errorTxt.write(str(e))
		errorTxt.write('\n')

def checkIn(account, pwd):
	print account + " begin"
	driver = webdriver.Firefox()
	driver.implicitly_wait(2)
	try:
		doCheckIn(driver, account, pwd)
		signClick(driver)
		pass
	except Exception, e:
		logError('etao checkIn failure', e)
		macNotify.notify("etao checkIn failure", account, str(e))
		pass
	else:
		pass
	finally:
		print account + " end"
		driver.quit()
		pass
