#Domain_Transfer

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

# countrandom+.dns1.managedns.org

Last2 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[2]/span/input').send_keys("oIVhI17Jbh")
sleep(2)
driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/button').click()
sleep(5)
#Place_Order
driver.find_element("xpath", '/html/body/div[1]/navside/div/ul/li[1]/a/span').click()
sleep(2)

#Domain_Transfer
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/ul/li[3]/a').click()
sleep(20)

#Transfer
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/div/div[2]/form/div[2]/button').click()
sleep(20)

#Refresh
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[1]/table/tfoot/tr[8]/th[6]/a/i').click()
sleep(2)

#Register
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[1]').click()
sleep(2)

#Back_to_Domain_page
driver.back()
sleep(2)
driver.refresh()
sleep(2)


#Place_Order
driver.find_element("xpath", '/html/body/div[1]/navside/div/ul/li[1]/a/span').click()
sleep(2)

#Domain_Transfer_with_code
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/ul/li[3]/a').click()
sleep(20)

#Transfer
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/div/div[2]/form/div[2]/button').click()
sleep(20)

#Use coupon code
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[8]/label[1]/input').click()
sleep(2)
#for more suggestion
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[8]/label[2]/input').click()
sleep(2)
#Register
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[1]').click()
sleep(2)

#Back_to_Domain_page
driver.back()
sleep(2)
driver.refresh()
sleep(2)

#Place_Order
driver.find_element("xpath", '/html/body/div[1]/navside/div/ul/li[1]/a/span').click()
sleep(2)

#Domain_Transfer_Search again
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/ul/li[3]/a').click()
sleep(20)

#Transfer
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[3]/div[2]/ng-form/div[2]/div/div/div/div[2]/form/div[2]/button').click()
sleep(20)

#Search again_Button
driver.find_element("xpath", '/html/body/div[1]/div/div[7]/div[10]/button[2]').click()
sleep(2)
#Domain transfer
driver.find_element("xpath", '/html/body/div[1]/div/div[10]/div[2]/ng-form/div[2]/div/div/ul/li[3]/a').click()
sleep(20)




#Tranfer
driver.find_element("xpath", '/html/body/div[1]/div/div[10]/div[2]/ng-form/div[2]/div/div/div/div[2]/form/div[2]/button').click()
sleep(2)




#
# driver.find_element("xpath", '').click()
# sleep(2)
# #
# driver.find_element("xpath", '').click()
# sleep(2)
# #
# driver.find_element("xpath", '').click()
# sleep(2)
# #
# driver.find_element("xpath", '').click()
# sleep(2)
# #
# driver.find_element("xpath", '').click()
# sleep(2)