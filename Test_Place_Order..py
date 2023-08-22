
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://beta.connectreseller.com")
sleep(5)
#login details 
my_username ="mayuresh.shinde@vertoz.com"
my_password = "oIVhI17Jbh"
Last1 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[1]/span/input').send_keys("mayuresh.shinde@vertoz.com")
sleep(5)


Last2 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[2]/span/input').send_keys("oIVhI17Jbh")
sleep(2)
driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/button').click()
sleep(2)

#Search for your domain(Register)
driver.find_element("xpath", '/html/body/div[1]/navside/div/ul/li[1]/a/span').click()
sleep(20)

driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/div/div[1]/form/div[2]/button').click()
sleep(5)
#Refresh
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[1]/table/tfoot/tr[8]/th[6]/a/i').click()
sleep(2)

#Register
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[1]').click()
sleep(5)
#Register_Yes
driver.find_element("xpath", '/html/body/div[1]/div/div[11]/form/div[3]/button[2]').click()
sleep(5)
#Back_to_Domain_page
driver.back()
sleep(2)
driver.refresh()
sleep(2)

#Search Again_Search for your domain(Register)

driver.find_element("xpath", '/html/body/div[1]/navside/div/ul/li[1]/a/span').click()
sleep(20)

driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/div/div[1]/form/div[2]/button').click()
sleep(5)


#Search Again
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[2]').click()
sleep(20)

#Search 
driver.find_element("xpath", '/html/body/div[1]/div/div[10]/div[2]/ng-form/div[2]/div/div/div/div[1]/form/div[2]/button').click()
sleep(5)

#manage_customer
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[1]/table/tbody/tr/td[3]/span[1]/a/img').click()
sleep(5)

#Manage Nameservers
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[1]/table/tbody/tr/td[3]/span[2]/a/img').click()
sleep(5)

#Manage Privacy Protection
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[1]/table/tbody/tr/td[3]/span[3]/a/img').click()
sleep(5)

#Use coupon code
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[8]/label[1]/input').click()
sleep(5)
#for more suggestion
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[8]/label[2]/input').click()
sleep(5)



#Add_more_1
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[3]').click()
sleep(20)

#Add_more_button
driver.find_element("xpath", '/html/body/div[1]/div/div[12]/form/div[2]/div[2]/div/div/ng-form/div[2]/button').click()
sleep(5)

#Add_more_2
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[3]').click()
sleep(20)

#Add_more_button
driver.find_element("xpath", '/html/body/div[1]/div/div[12]/form/div[2]/div[2]/div/div/ng-form/div[2]/button').click()
sleep(5)

#Add_more_3
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[3]').click()
sleep(20)

#Add_more_button
driver.find_element("xpath", '/html/body/div[1]/div/div[12]/form/div[2]/div[2]/div/div/ng-form/div[2]/button').click()
sleep(5)

#Register_button
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[1]').click()