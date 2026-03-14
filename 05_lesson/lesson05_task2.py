from time import sleep    
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://uitestingplayground.com/dynamicid')

for i in range(3):
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    driver.refresh()

driver.quit()
