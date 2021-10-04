import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC

class usando_unittesst(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

  def test_usanddo_implicit_wait(self):
    driver =self.driver
    driver.implicitly_wait(10) #segundos                
    driver.get("http://www.google.com")
    myDynamicElement = driver.find_element_by_name("q")

if __name__ == '__main__':
  unittest.main()