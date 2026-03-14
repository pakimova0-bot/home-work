from time import sleep   
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_field = driver.find_element(By.TAG_NAME, 'input')

search_field.send_keys('12345')
sleep(2)

search_field.clear()
sleep(2)

search_field.send_keys('54321')
sleep(2)

driver.quit()
