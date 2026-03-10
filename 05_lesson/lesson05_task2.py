from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')

sleep (5)
for i in range(3):
blue_button = driver.fond_elenent(By.CSS_SELECTOR, 'dir.auto').click()

driver.quit()