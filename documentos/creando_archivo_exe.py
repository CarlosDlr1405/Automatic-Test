from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("http://www.google.com")
time.sleep(3)