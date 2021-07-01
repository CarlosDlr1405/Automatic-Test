import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#creando una clase
class usando_unittest(unittest.TestCase):
    
	def setUp(self):                #ruta del webdriver
		self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

	def test_buscar_por_xpath(self):
		driver=self.driver
		driver.get("http://www.google.com")
		time.sleep(10)
		buscar_por_xpath=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
		time.sleep(10)
		buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
		time.sleep(10)
   #para cerrar el navegador
	def tearDown(self):
		self.driver.close()

	#Para correr el test case
if __name__ == '__main__':
	unittest.main()