import unittest
from unittest.case import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):
  def setUp(self):
    self.driver= webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    
  def test_login(self):
    driver=self.driver
    driver.get("https://www.w3schools.com")
    time.sleep(3)
    btn=driver.find_element_by_id("w3loginbtn")
    btn.click()
    usuario=driver.find_element_by_id("modalusername")
    usuario.send_keys("cdelarosa@ucol.mx")
    contraseña=driver.find_element_by_id("current-password")
    contraseña.send_keys("Carlososwaldo05%")
    iniciar=driver.find_element_by_xpath("//*[@id='root']/div/div/div[4]/div[1]/div/div[4]/div[1]/button")
    iniciar.click()
    time.sleep(3)

if __name__=='__main__':
  unittest.main()