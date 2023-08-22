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
my_password = "oIVhI17Jbh"
Last1 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[1]/span/input').send_keys("mayuresh.shinde@vertoz.com")
sleep(5)
Last2 = driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/label[2]/span/input').send_keys("oIVhI17Jbh")
sleep(5)

driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/label/input').click()
sleep(5)
#
driver.find_element("xpath", '/html/body/div/div/div/div/div/div[3]/div/div/div/div[2]/form/fieldset[1]/div[2]/button').click()
sleep(5)
################################################################


#Box 
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/input').click()
sleep(5)
#Renew button
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/button').click()
sleep(5)
#Renewal_Term_Drop_Down
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr/td[4]').click()
sleep(5)
#Renew
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/button').click()
sleep(5)
#Click 'Yes'
driver.find_element("xpath", '/html/body/div[1]/div/div[4]/form/div[3]/button[2]').click()
sleep(5)
#Back_to_Domain_page
driver.back()
sleep(2)
driver.refresh()
sleep(2)

#Select
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/input').click()
sleep(2)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/input').click()
sleep(2)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[1]/input').click()
sleep(2)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/input').click()
sleep(2)
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[5]/td[1]/input').click()
sleep(2)
#Renew button
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/button').click()
sleep(5)

#Drop_Down  
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[4]').click()
sleep(5)
#@
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/thead/tr/th[4]').click()


driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[2]/td[4]').click()
sleep(5)
#@
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/thead/tr/th[4]').click()

driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[3]/td[4]').click()
sleep(5)
#@
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/thead/tr/th[4]').click()

driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[4]/td[4]').click()
sleep(5)
#@
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/thead/tr/th[4]').click()

driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[5]/td[4]').click()
sleep(5)
#@
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/table/thead/tr/th[4]').click()

#Renew
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/button').click()
sleep(5)

driver.find_element("xpath", '/html/body/div[1]/div/div[4]/form/div[3]/button[2]').click()
sleep(5)

# driver.get_screenshot_as_file("DOMAIN Renew")
# sleep(5)
#Back_to_Domain_page
driver.back()
sleep(2)
driver.refresh()
sleep(2)

# #Select
# driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/input').click()
# sleep(2)
# driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/input').click()
# sleep(2)
# driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[3]/td[1]/input').click()
# sleep(2)
# driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/input').click()
# sleep(2)
# driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/table/tbody/tr[5]/td[1]/input').click()
# sleep(2)
# #Renew button
driver.find_element("xpath", '/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div/button').click()
sleep(2)






# driver.find_element(by.css_selector, "element_css_selector")

#Coupon code
