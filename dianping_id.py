# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import macNotify
import sys

def writeCode(account):
	for cookie in driver.get_cookies():
		if(cookie['name'] == "dper"):
			with open('dp.code.txt','a') as txt:
				line = account + ' ' + cookie['value'] + '\n'
				txt.write(line)
				print line	

def sendViewCode():
	try:
		inputElement = driver.find_element_by_id("code")
		input_seccode=unicode(raw_input('enter:'))
		pass
	except Exception, e:
		print 'no view code'
		pass
	else:
		inputElement.send_keys(input_seccode)
		pass
	finally:
		pass

def doCheckIn(account, pwd):
	inputElement = driver.find_element_by_id("user")
	inputElement.send_keys(account)
	print inputElement.text
	inputElement = driver.find_element_by_id("password")
	inputElement.send_keys(pwd)
	sendViewCode()
	inputElement = driver.find_element_by_class_name("btn")
	inputElement.click()

	driver.implicitly_wait(3)

#	inputElement = driver.find_element_by_class_name("loginSuccess")
#	print account + ":" + inputElement.text

def checkIn(account, pwd):
	driver.delete_all_cookies()
	driver.get("http://www.dianping.com/login")
	# find the element that's name attribute is q (the google search box)
	try:
		doCheckIn(account, pwd)
		writeCode(account)
		pass
	except Exception, e:
		print e
		try:
			macNotify.notify('check in failure', account, e)
			pass
		except Exception, notifyE:
			print notifyE
		pass
	else:
		pass
	finally:
		pass

def checkByCode():
	with open('dpid.code.txt') as codeTxt:
	    for line in codeTxt:
	    	if(line.startswith('#')):
	    		continue
	        nos = line.rstrip().split(' ')
	        account, pwd = nos[0], nos[1]
	        checkIn(account, pwd)

reload(sys) 
sys.setdefaultencoding('utf8')
driver = webdriver.Firefox()
#driver.get("http://www.dianping.com/beijing")
checkByCode()
driver.quit()
