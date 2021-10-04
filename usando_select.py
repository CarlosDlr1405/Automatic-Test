import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
import time

class usando_unittest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

  def test_usando_select(self):
    driver= self.driver
    driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
    time.sleep(4)
    select=driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
    opcion= select.find_elements_by_tag_name("option")
    time.sleep(2)
    for option in opcion:
      print("los valoresa son: %s" % option.get_attribute("value"))
      option.click()
      time.sleep(2)
    seleccionar= Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
    seleccionar.select_by_value("8")
    time.sleep(5)

if __name__ == '__main__':
  unittest.main()
