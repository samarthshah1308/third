from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print("Url is accesible")
time.sleep(3)
def login():

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    print(" Enter your User name")
    time.sleep(3)

    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    print(" Enter your Password")
    time.sleep(3)

    driver.find_element(By.ID,"login-button").send_keys(Keys.ENTER)
    print("Login button clicked")
    time.sleep(3)

def sorting():   
    driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()
    print("Sort By Price (high to low)")
    time.sleep(3)

def add_cart():
    driver.find_element(By.ID,"remove-sauce-labs-backpack").send_keys(Keys.ENTER)
    print("Add to Cart")
    time.sleep(3)

    driver.find_element(By.ID,"shopping_cart_container").click()
    print("Open Cart")
    time.sleep(3)

def checkout():
    driver.find_element(By.ID,"checkout").click()
    print("Checkout")
    time.sleep(3)

    driver.find_element(By.ID,"first-name").send_keys("Hemali")
    print("first Name")
    time.sleep(3)

    driver.find_element(By.ID,"last-name").send_keys("Thakkar")
    print("Last Name")
    time.sleep(3)

    driver.find_element(By.ID,"postal-code").send_keys("382350")
    print("Zip Code")
    time.sleep(3)

    driver.find_element(By.ID,"continue").click()
    print("Continue")
    time.sleep(3)

    driver.find_element(By.ID,"finish").click()
    print("Finish")
    time.sleep(3)

login()
sorting()
add_cart()
checkout()

driver.close()