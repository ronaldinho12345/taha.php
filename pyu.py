from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("Asif SK")
password = browser.find_element_by_id("taha66")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("tahakourani88@gmail.com")
password.send_keys("taha2003")
# Step 4) Click Login
submit.click()
