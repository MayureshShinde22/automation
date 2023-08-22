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
        sleep(1)
        
        password=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[2]/span/input')
        password.send_keys(my_password)
        sleep(1)
        
        loginButtonRem=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/label/input')
        loginButtonRem.click()
        sleep(1)
        
        loginButton=driver.find_element(By.XPATH, '//html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/button')
        loginButton.click()
        sleep(1)
        print("Login completed !!!!!!")

        customerTab=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[5]/a[2]/span')
        customerTab.click()
        sleep(5)
        
        customerSelect1=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div/div[4]/div/table/tbody/tr[1]/td[2]/a/u')
        customerSelect1.click()
        sleep(2)
        print ("1st customer selected")
        
        domainList=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[2]/a')
        domainList.click()
        sleep(2)
        
        ContactManagement=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[3]/a')
        ContactManagement.click()
        sleep(2)
        
        LoginToPanel=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[4]/a')
        LoginToPanel.click()
        sleep(2)
        
        
        
        LoginTocustomerPanelbutton=driver.find_element(By.XPATH, '//*[@id="home"]/div/div/div/div/button')
        LoginTocustomerPanelbutton.click()
        sleep(5)
        print ("Login to customer panel complete")
        CustomerSetting=driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div/ul/li[7]/a/i[2]')
        CustomerSetting.click()
        sleep(5)
        
        ActionHistory=driver.find_element(By.XPATH, '/html/body/navtop/div/div/div/ul/li[7]/ul/li[2]/a')
        ActionHistory.click()
        sleep(5)
        
        EmailHistory=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/ul/li[2]/a')
        EmailHistory.click()
        sleep(5)
        
        ViewEmailDetails=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/table/tbody/tr[1]/td[5]/div/button[2]/i')
        ViewEmailDetails.click()
        sleep(5)
        
        BackToEmail_History=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/ul/li[1]/a')
        BackToEmail_History.click()
        sleep(5)
        print ("Email History completed")
        CustomerSetting=driver.find_element(By.XPATH, '/html/body/navtop/div/div/div/ul/li[7]/a/i[2]')
        CustomerSetting.click()
        sleep(5)
        
        profileSetting=driver.find_element(By.XPATH, '/html/body/navtop/div/div/div/ul/li[7]/ul/li[3]/a')
        profileSetting.click()
        sleep(5)
        
        PasswordSetting=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[2]/a')
        PasswordSetting.click()
        sleep(5)
        
        ContactManagement=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[8]/a')
        ContactManagement.click()
        sleep(5)
        
        ContactUser=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/div/div[11]/div/div[2]/div/table/tbody/tr/td[2]/a/u')
        ContactUser.click()
        sleep(5)
        print ("Profile settings completed")

        BackToprofilepage=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/ul/li[1]/a')
        BackToprofilepage.click()
        sleep(5)
        
        BackToRE_login=driver.find_element(By.XPATH, '/html/body/navtop/div/div/div/ul/li[2]/a')
        BackToRE_login.click()
        sleep(5)
        print ("Back to Reseller_login page")
        
        Customer=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[5]/a[2]/span')
        Customer.click()
        sleep(5)
        
        secondCustomer=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div/div[4]/div/table/tbody/tr[2]/td[2]/a/u')
        secondCustomer.click()
        sleep(5)
        
        BackToCu_list=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/ul/li[1]/a')
        BackToCu_list.click()
        sleep(5)
        
        
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        # =driver.find_element(By.XPATH, '')
        # .click()
        # sleep(5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        print("Task_completed !!!!!!")
        
        
        
        
    except ValueError:
        print("tested... error")


Login()

