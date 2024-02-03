# ------------- Imports Done Here ---------
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = None

def start():
    #  --------URL-------
    global driver
    driver = webdriver.Chrome()
    url = "https://orteil.dashnet.org/cookieclicker/"
    driver.get(url)


def select_lang():
    # ------- Select Language -------
    language_select = driver.find_element(By.ID,"langSelect-EN")
    language_select.click()
    time.sleep(10)


def play_game():
    #   ------------ Get Elements --------- 
    cookie = driver.find_element(By.ID, "bigCookie")
    cursor = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]")
    product_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[3]")
    product_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[4]")
    product_3 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[5]")
    
    while (True):
        print("Clicking Items")
        #   ------------ Click Cookie and Buy Products --------- 
        cookie.click()
        # cursor.click()
        # product_3.click()
        # product_2.click()
        # product_1.click()

            
def driver():
    start()
    time.sleep(5)
    select_lang()
    play_game()


driver()