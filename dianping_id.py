from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def writeCode(account):
	for cookie in driver.get_cookies():
		if(cookie['name'] == "dper"):
			with open('dp.code.txt','a') as txt:
				line = account + ' ' + cookie['value'] + '\n'
				txt.write(line)
				print line	

def doCheckIn(account, pwd):
	inputElement = driver.find_element_by_id("J_usrname")
	inputElement.send_keys(account)
	print inputElement.text
	inputElement = driver.find_element_by_id("J_pwd")
	inputElement.send_keys(pwd)
	input_seccode=raw_input('enter:')
	inputElement = driver.find_element_by_id("J_validate")
	inputElement.send_keys(input_seccode)
	
	inputElement = driver.find_element_by_id("J_login-btn")
	inputElement.click()

	driver.implicitly_wait(3)
	inputElement = driver.find_element_by_class_name("loginSuccess")
	print account + ":" + inputElement.text

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
		pass
	else:
		pass
	finally:
		pass

def checkByCode():
	with open('dpid.code.txt') as codeTxt:
	    for line in codeTxt:
	        nos = line.rstrip().split(' ')
	        account, pwd = nos[0], nos[1]
	        checkIn(account, pwd)

driver = webdriver.Firefox()
#driver.get("http://www.dianping.com/beijing")
checkByCode()
driver.quit()
