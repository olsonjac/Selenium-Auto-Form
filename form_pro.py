import time
import names
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#necessary selenium options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("-incognito")
service = ChromeService(executable_path='Path_to_chromedriver')
driver = webdriver.Chrome(service=service, options=options)
#asks the user for the number of times they want to fill out the form
fills = int(input("how many times do you want to fill the form out? "))
fills = fills + 1
#separates the whole process into a function that can be run multiple times
def all():
  #designates the url of the form being filled out
  driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdBt1_lZ6PwozDEBVuUxl50EwEmKW6cKs9gwEpUvMiCkMky3Q/viewform")
  #This prints the title of the page as a test that the URL is good
  print(driver.title)
  #This located all available checkboxes on the form
  checkbox1 = driver.find_element(By.CLASS_NAME, "D8bnZd")
  checkbox2 = driver.find_element(By.XPATH, "//*[@id=\"i12\"]/div[3]/div")
  checkbox3 = driver.find_element(By.XPATH, "//*[@id=\"i15\"]/div[3]/div")
  checkbox4 = driver.find_element(By.XPATH, "//*[@id=\"i18\"]/div[3]/div")
  #Creates a list of all 4 checkbox options
  checks = [checkbox1,checkbox2,checkbox3,checkbox4]
  #This locates the name entry text box
  namebox = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
  #This locates the submission button
  submitbutton = driver.find_element(By.XPATH, "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
  time.sleep(1)
  #Generates a random first and last name to input
  rand_name = names.get_full_name()
  #sends the random name to the namebox input
  namebox.send_keys(rand_name)
  #picks a random checkbox from the 4 options
  random.choice(checks).click()
  #submits the form 
  submitbutton.click()
  #finds and clicks the "submit another form button at the end
  resubmitbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
  resubmitbutton.click()
# for loop that submits the form as many times as directed
for i in range(fills):
  all()

