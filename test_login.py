import os
import time
from selenium import webdriver
import unittest
import HTMLTestRunner
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class Login(unittest.TestCase):
	def setUp(self):

		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '5.0.1'
		desired_caps['deviceName'] = '64dfda86'
		desired_caps['app'] = PATH('C:/pythonex\Jufan_test/JuFan-1.2.0-095-52.apk')
		desired_caps['app-package'] = 'com.guagua.live'
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		self.driver.quit()



	def test_login(self):
		driver.findElement_by_id()



		

#if __name__ == '__main__':
	# unittest.main()