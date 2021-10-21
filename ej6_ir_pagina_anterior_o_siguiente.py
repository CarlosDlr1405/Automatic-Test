import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
	
	
	def setUp(self):
		self.driver= webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
	
	
	def test_siguiente(self):
		driver=self.driver
		driver.cbget("http://www.google.com")
		time.sleep(3)
		driver.get("http://www.youtube.com")
		time.sleep(3)
		driver.get("https://www.facebook.com/")
		time.sleep(3)
		#comando para ir a pagina anterior
		driver.back()
		time.sleep(3)
		driver.back()
		time.sleep(3)
		driver.back()
		time.sleep(3)
		#comando para ir a pagina siguente
		driver.forward()
if __name__ == '__main__':
	unittest.main()


