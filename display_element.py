import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(15)
display_element=driver.find_element_by_name("btnI")
print(display_element.is_displayed())#Arroja un valor booleano si el elemento ya cargo
print(display_element.is_enabled())#Arroja un valor booleano si el elemento esta disponible