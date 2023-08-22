##Domain_functions
from select import select
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://beta.connectreseller.com")
sleep(5)
#login details 
my_username ="mayuresh.shinde@vertoz.com"
my_password = "Test@1998"


try:
    
    Last1 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[1]/span/input').send_keys("mayuresh.shinde@vertoz.com")
    sleep(5)
    Last2 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[2]/span/input').send_keys("Test@1998")
    sleep(5)

    driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/label/input').click()
    sleep(5)
    #LOGIN
    driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/button').click()
    sleep(5)
    print("Log_in succesfully")

    #Domain_page
    driver.find_element("xpath", '/html/body/div[1]/navside/div/ul/li[4]/a[2]/span').click()
    sleep(5)
    #domain_name
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/span/a/u').click()
    sleep(2)
      
    ################################################################
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    # Manage Domain
    # 1.Name Servers
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[1]/div[1]/a').click()
    sleep(2)
    # 2.Child Name Servers 
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[2]/div[1]/a').click()
    sleep(2)
    # 3. Contact Details  
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[3]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[3]/div[1]/a').click()
    sleep(2)
    # 4.Theft Protection 
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[4]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[4]/div[1]/a').click()
    sleep(2)
    # 5.DNS Management Panel
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[5]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[5]/div[1]/a').click()
    sleep(2)
    #6.Privacy Protection 
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[6]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[6]/div[1]/a').click()
    sleep(2)
    # 7.Domain Secret 
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[7]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[7]/div[1]/a').click()
    sleep(2)
    #8.Domain lock and Suspend
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[8]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[8]/div[1]/a').click()
    sleep(2)
    #9.Domain Forwarding

    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[9]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[9]/div[1]/a').click()
    sleep(2)
    #10.  GDPR Protection 

    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[10]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[10]/div[1]/a').click()
    sleep(2)
    #11. Move Domain 
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[11]/div[1]/a').click()
    sleep(2)
    #Click_Off
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[11]/div[1]/a').click()
    sleep(2)
    #12.DNSSEC
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[12]/div[1]/a').click()
    sleep(2)
    # #Click_Off
    # driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div[2]/div[12]/div[1]/a').click()
    # sleep(2)
    #################################################################################**********
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    ###############################
    ##Multiple_Domain
    #Renew_Domain

    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   
    
    #Renew
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[3]').click()
    
    sleep(2)
    
    #Renew button
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/button').click()
    
    sleep(2)
    
    #Renew_Yes
    driver.find_element("xpath", '/html/body/div[1]/div/div[4]/form/div[3]/button[2]').click()

    sleep(2)
    print("Renew succesfully")
    
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    
    #Suspend_Domain
    
    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   

    #Suspend
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[4]').click()
    sleep(2)
    
  
    print("Suspend succesfully")
    
    
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    
    #Unsuspend_Domain
    
    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   

    #Unsuspend
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[5]').click()
    sleep(2)
    
    print("Unsuspend succesfully")
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    
    
    #lock_Domain
    
    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   

    #lock
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[6]').click()
    sleep(2)
    
    print("Lock succesfully")
    
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    
    
    #Unlock_Domain
    
    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   
    #Unlock
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[7]').click()
    sleep(2)
    
    print("Unlock succesfully")
      
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    
    #Update_NS_Domain
    
    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   

    #Update_NS
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[8]').click()
    sleep(2)
    
    print("Update_NS succesfully")
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)
    
    #Move_Domain
    
    #Select domain_1
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[2]/td[1]/input').click()
    sleep(2)
    #Select domain_2
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[3]/td[1]/input').click()
    sleep(2)
    #Select domain_3
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/input').click()
   

    #Move
    driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/button[9]').click()
    sleep(2)
    
    print("Move succesfully")
      
    #Back_to_Domain_page
    driver.back()
    sleep(2)
    driver.refresh()
    sleep(2)

    
    
    # #
    # driver.find_element("xpath", '').click()
    
    # sleep(2)
    
    
    
    
    # #

    # driver.find_element("xpath",'//*[@id="renew-button"]').click()
    
    # logout= 
    
    
    # driver.close()
    print("run succesfully")


    
except ValueError:
    print("error")
# driver.find_element("xpath", '').click()
# sleep(2)

# #
# driver.find_element("xpath", '').click()
# sleep(2)
# #
# driver.find_element("xpath", '').click()
# sleep(2)


