from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import warnings
import time


warnings.filterwarnings(action='ignore', category=DeprecationWarning) # setting ignore as a parameter and further adding category

username = ""
password = ""

def user_pass():
	while True:
		username = input(" Enter username : ")
		if username != "":
			break
		else:
			print(" Username can not be blank !!! ")
			continue
	while True:
		password = input(" Enter password : ")
		if password != "":
			break
		else:
			print(" Password can not be blank !!! ")
			continue

def connection():
	#PATH FOR CHROMEDRIVER
	driver = webdriver.Chrome(executable_path=r'E:\\chromedriver.exe')


	base_url = 'http://127.0.0.1:8000'
	driver.get(base_url)
	driver.maximize_window()
	#enter username and password
	driver.find_element_by_id("username").clear()
	driver.find_element_by_id("username").send_keys(username)
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys(password)
	#adding data
	driver.find_element_by_css_selector("input.splButton-primary.btn").click()
	driver.find_element_by_id('AddData').click()
	#uploading data
	#file 1
	driver.find_element_by_class_name('type-text1------dev---2COVu').click()
	time.sleep(2)
	driver.find_element_by_id('inputReference').send_keys("E:\\UNIVERSITY\\SEM - 7\\SECURITY INFORMATION & EVENT MANAGEMENT\\PROJECT\\Application_Log.csv")
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	#add file 2
	driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[5]/a').click()
	#file 2
	driver.find_element_by_class_name('type-text1------dev---2COVu').click()
	time.sleep(2)
	driver.find_element_by_id('inputReference').send_keys("E:\\UNIVERSITY\\SEM - 7\\SECURITY INFORMATION & EVENT MANAGEMENT\\PROJECT\\System_Log.csv")
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	#add file 3
	driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[5]/a').click()
	#file 3
	driver.find_element_by_class_name('type-text1------dev---2COVu').click()
	time.sleep(2)
	driver.find_element_by_id('inputReference').send_keys("E:\\UNIVERSITY\\SEM - 7\\SECURITY INFORMATION & EVENT MANAGEMENT\\PROJECT\\Security_Log.csv")
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wizard-placeholder"]/div/div[6]/a[2]/span').click()
	time.sleep(2)
	#start searching
	driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[3]/a').click()
	time.sleep(15)


#user_pass()
#connection()