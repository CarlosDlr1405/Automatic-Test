from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("http://www.google.com")
time.sleep(3)
dato= driver.find_element_by_link_text("Privacidad")

#simula la posicion del puntero.
hover=ActionChains(driver).move_to_element(dato)
hover.perform()

