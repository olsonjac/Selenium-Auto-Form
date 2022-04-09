import time
import names
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("-incognito")
service = ChromeService(executable_path='/home/jacob/Downloads/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

def all():
  driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdBt1_lZ6PwozDEBVuUxl50EwEmKW6cKs9gwEpUvMiCkMky3Q/viewform")
  print(driver.title)
# This located all available checkboxes on the form
  checkbox1 = driver.find_element(By.CLASS_NAME, "D8bnZd")
  checkbox2 = driver.find_element(By.XPATH, "//*[@id=\"i12\"]/div[3]/div")
  checkbox3 = driver.find_element(By.XPATH, "//*[@id=\"i15\"]/div[3]/div")
  checkbox4 = driver.find_element(By.XPATH, "//*[@id=\"i18\"]/div[3]/div")
  checks = [checkbox1,checkbox2,checkbox3,checkbox4]
#This locates the name entry text box
  namebox = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
#This locates the submission button
  submitbutton = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
#Submit another form
  time.sleep(1)
  rand_name = names.get_full_name()


  time.sleep(1)
  namebox.send_keys(rand_name)

  random.choice(checks).click()

  submitbutton.click()
  resubmitbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")

  resubmitbutton.click()

for i in range(10):
  all()

