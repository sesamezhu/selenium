from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import macNotify
import datetime
import sys

def doCheckIn(account):
	inputElement = driver.find_element_by_css_selector(".J_signbtn>a")
	print inputElement.text
	inputElement.click()
	print account + ":" + inputElement.text

def logError(message, e):
	print message
	print e
	with open('error.code.txt', 'a') as errorTxt:
		errorTxt.write(str(datetime.datetime.now()))
		errorTxt.write(message)
		errorTxt.write(str(e))
		errorTxt.write('\n')

def checkIn(account, dper):
	driver.add_cookie({'name':'dper', 'value':dper, 'path':'/'})
	driver.get("http://www.dianping.com/shanghai")
	# find the element that's name attribute is q (the google search box)
	try:
		doCheckIn(account)
		pass
	except Exception, e:
		logError('checkIn failure', e)
		macNotify.notify("checkIn failure", account, str(e))
		pass
	else:
		pass
	finally:
		pass

def checkByCode():
	with open('dp.code.txt') as codeTxt:
	    for line in codeTxt:
	        nos = line.rstrip().split(' ')
	        account, dper = nos[0], nos[1]
	        checkIn(account, dper)

reload(sys) 
sys.setdefaultencoding('utf8')
driver = webdriver.Firefox()
driver.get("http://www.dianping.com/beijing")
checkByCode()
driver.quit()
