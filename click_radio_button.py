import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

  def test_usando_radio_button(self):
    driver = self.driver
    driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
    time.sleep(3)
    radio_button= driver.find_element_by_xpath("//*[@id='main']/div[3]/div[2]/label[3]/span")
    radio_button.click()
    time.sleep(3)
    radio_button= driver.find_element_by_xpath("//*[@id='main']/div[3]/div[2]/label[1]")
    radio_button.click()
    time.sleep(3)

  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main()
