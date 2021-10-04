from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(3)
encuentra_link=driver.find_element_by_link_text('HTML Colors')
encuentra_link.click()