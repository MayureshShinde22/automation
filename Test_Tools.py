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
        
        print("Login successfully!")
        
        
        
        
        Tools=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[1]/span')
        Tools.click()
        sleep(5)
        
        Action_History=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[1]/a')
        Action_History.click()
        sleep(5)
        
        print("Action_History successfully!")
        
        OrderId_1=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[6]/div/table/tbody/tr[1]/td[2]/span/a')
        OrderId_1.click()
        sleep(5)
        
        BackTo_DH=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/ul/li[1]/a')
        BackTo_DH.click()
        sleep(5)
        
        Your_History=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/ul/li[1]/a')
        Your_History.click()
        sleep(5)
        
        Email_history=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/ul/li[2]/a')
        Email_history.click()
        sleep(5)
        print("Domain History successfully!")
        #Domain_Pull_Request

        Domain_Pull_Request=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[4]/a')
        Domain_Pull_Request.click()
        sleep(5)
        
        Domain_Pull_Request=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/ul/li[1]/a')
        Domain_Pull_Request.click()
        sleep(5)
        
        Profile_setting=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[5]/a')
        Profile_setting.click()
        sleep(5)
        
        
        Edit_password=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[2]/a')
        Edit_password.click()
        sleep(5)
        
        domainPricing=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[3]/a')
        domainPricing.click()
        sleep(5)
        
        Branding=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[4]/a')
        Branding.click()
        sleep(5)
        
        Branding_logo=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/div/div[5]/ul/li[2]/a')
        Branding_logo.click()
        sleep(5)
        
        Branding_DNS=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/div/div[5]/ul/li[3]/a')
        Branding_DNS.click()
        sleep(5)
        
        panelsetting=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[5]/a')
        panelsetting.click()
        sleep(5)
        
        API_key=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[6]/a/i')
        API_key.click()
        sleep(5)
        
        Use_TwoFactor_Authentication=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/form/div/ul/li[7]/a')
        Use_TwoFactor_Authentication.click()
        sleep(5)
        print("Profile_Setting successfully!")
        
        Domain_TransferOut_List=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[6]/a')
        Domain_TransferOut_List.click()
        sleep(5)
        print("Domain_TransferOut_List successfully!")
        Pending_Bulk_Summary=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[7]/a')
        Pending_Bulk_Summary.click()
        sleep(5)
        print("Pending_Bulk_Summary successfully!")

        Premium_Domain=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[14]/a')
        Premium_Domain.click()
        sleep(5)
        print("Premium_Domain successfully!")
        Reports=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[17]/a')
        Reports.click()
        sleep(5)
        print("Reports successfully!")
        Bulk_actionFile_Upload=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[19]/a')
        Bulk_actionFile_Upload.click()
        sleep(5)
        print("Bulk_actionFile_Upload successfully!")
        CouponReports=driver.find_element(By.XPATH, '/html/body/div[1]/navside/div/ul/li[11]/div[2]/div/ul/li[22]/a')
        CouponReports.click()
        sleep(5)
        
        print("CouponReports successfully!")
        
        Dropdown=driver.find_element(By.XPATH, '/html/body/navtop/div/div/div/ul/li[7]/a')
        Dropdown.click()
        sleep(5)
        
        Logout=driver.find_element(By.XPATH, '/html/body/navtop/div/div/div/ul/li[7]/ul/li[10]/a')
        Logout.click()
        sleep(5)
        print("Logout successfully!")
       
        
        
        
        print("completed !!!!!!")
        
        
        
        
    except ValueError:
        print("tested... error")


Login()
