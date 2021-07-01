from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

driver.get("https://siceuc.ucol.mx")

usuario = driver.find_element_by_name("txtCuenta")
usuario.send_keys("20134456")

contraseña = driver.find_element_by_name("txtPassword")
contraseña.send_keys("carlososwaldo05")
contraseña.send_keys(Keys.ENTER)
time.sleep(15)
driver.close() 