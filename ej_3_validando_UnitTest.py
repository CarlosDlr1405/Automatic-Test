<<<<<<< HEAD
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
	"""docstring for usando_unittest"""
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
	def test_buscar(self):
		driver=self.driver
		driver.get("http://google.com")
		self.assertIn("Google", driver.title)
		elemento=driver.find_element_by_name("q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)
		time.sleep(10)
		assert "no se identifico el elemento" not in driver.page_source
	def tearDown(self):
		self.driver.close()
if __name__ == '__main__':
=======
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
	"""docstring for usando_unittest"""
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
	def test_buscar(self):
		driver=self.driver
		driver.get("http://google.com")
		self.assertIn("Google", driver.title)
		elemento=driver.find_element_by_name("q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)
		time.sleep(10)
		assert "no se identifico el elemento" not in driver.page_source
	def tearDown(self):
		self.driver.close()
if __name__ == '__main__':
>>>>>>> 74bafdbc1189f03589e1608ff28c0ea9d72ea7bf
	unittest.main()