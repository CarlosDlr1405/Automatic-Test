<<<<<<< HEAD
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class usando_unittest(unittest.TestCase):
	#funcion para cargar el driver
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

	def test_cambiar_ventanas(self):
		#mando a llamar a mi variable drive
		driver=self.driver
		         #ventana0
		driver.get("http://google.com")
		time.sleep(3)
		#comando para abrir una una nueva ventana,ventana1
		driver.execute_script("window.open('');")
		time.sleep(3)
		#comando cambiar a,handles:seleccionar la ventana (1)
		driver.switch_to.window(driver.window_handles[1])
		driver.get("https://www.youtube.com/")
		time.sleep(5)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(5)
	

if __name__ == '__main__':
=======
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class usando_unittest(unittest.TestCase):
	#funcion para cargar el driver
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

	def test_cambiar_ventanas(self):
		#mando a llamar a mi variable drive
		driver=self.driver
		         #ventana0
		driver.get("http://google.com")
		time.sleep(3)
		#comando para abrir una una nueva ventana,ventana1
		driver.execute_script("window.open('');")
		time.sleep(3)
		#comando cambiar a,handles:seleccionar la ventana (1)
		driver.switch_to.window(driver.window_handles[1])
		driver.get("https://www.youtube.com/")
		time.sleep(5)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(5)
	

if __name__ == '__main__':
>>>>>>> 74bafdbc1189f03589e1608ff28c0ea9d72ea7bf
	unittest.main()