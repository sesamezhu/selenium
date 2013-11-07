from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.dianping.com")
#driver.add_cookie({'name':'dper', 'value':'72c352db67f3e7e7a582cc4f3d9e5ad0bc1f58dc71cc900728c0b5294d67c79a', 'path':'/'})
driver.add_cookie({'name':'dper', 'value':'414ff6c94ce01d9a9a4bf7f46ac3c8df1cb2289ee288b9ebf08166956add8433', 'path':'/'})
driver.get("http://www.dianping.com/shanghai")

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_css_selector(".J_signbtn>a")
print inputElement.text
inputElement.click()
print inputElement.text
driver.quit()