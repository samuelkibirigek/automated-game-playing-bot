from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service("C:/Users/Sam/Desktop/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 60*5  # 5 minutes from now
upgrade_check = 5


while True:
    cursor_price = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split()[2])
    grandma_price = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split()[2])
    factory_price = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split()[2])
    mine_price = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split()[2].replace(",", ""))
    shipment_price = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split()[2].replace(",", ""))
    alchemy_price = int(driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split()[3].replace(",", ""))
    portal_price = int(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text.split()[2].replace(",", ""))
    timeMachine_price = int(driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.split()[3].replace(",", ""))

    cookie.click()
    if time.time() > upgrade_check:
        money = int(driver.find_element(By.ID, "money").text)
        if money > 15 and cursor_price < 25:
            cursor = driver.find_element(By.ID, "buyCursor")
            cursor.click()
        elif money > 111 and grandma_price < 150:
            cursor = driver.find_element(By.ID, "buyGrandma")
            cursor.click()
        elif money > 500 and factory_price < 600:
            cursor = driver.find_element(By.ID, "buyFactory")
            cursor.click()
        elif money > 2000:
            cursor = driver.find_element(By.ID, "buyMine")
            cursor.click()
        elif money > 7000:
            cursor = driver.find_element(By.ID, "buyShipment")
            cursor.click()
        elif money > 50000:
            cursor = driver.find_element(By.ID, "buyAlchemy lab")
            cursor.click()
        elif money > 1000000:
            cursor = driver.find_element(By.ID, "buyPortal")
            cursor.click()
        elif money > 123456789:
            cursor = driver.find_element(By.ID, "buyTime machine")
            cursor.click()
        else:
            continue


    if time.time() > timeout:
        cookies_per_second = driver.find_element(By.ID, "cps").text
        print(cookies_per_second)
        break


