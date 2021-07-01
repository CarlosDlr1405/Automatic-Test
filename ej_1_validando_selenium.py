from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

driver.get("https://siceuc.ucol.mx")
time.sleep(10)
driver.close() 