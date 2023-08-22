from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

def Login() :

    options =  webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/home/tr-dt-094/Downloads/chromedriver" , options=options)
    driver.maximize_window()
    driver.get("https://beta.connectreseller.com")
    sleep(5)
    #login details 
    my_username ="mayuresh.shinde@vertoz.com"
    my_password = "oIVhI17Jbh"

    try:
        
        username=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[1]/span/input')
        username.send_keys(my_username)
        sleep(5)
        
        password=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[2]/span/input')
        password.send_keys(my_password)
        sleep(5)
        
        loginButtonRem=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/label/input')
        loginButtonRem.click()
        sleep(5)
        
        loginButton=driver.find_element(By.XPATH, '//html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/button')
        loginButton.click()
        sleep(5)
        

        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        =driver.find_element(By.XPATH, '')
        .click()
        sleep(5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        print("completed !!!!!!")
        
        
        
        
    except ValueError:
        print("tested... error")


Login()
