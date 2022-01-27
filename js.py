from selenium import webdriver
from time import sleep
class facebookLogin:
  def __init__(self):
      self.driver=webdriver.Chrome()
      self.driver.get("https://www.facebook.com/")
      self.driver.find_element_by_xpath('')
      facebookLogin()