import selenium
import time 
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
wait = WebDriverWait(driver , 100 )
driver.maximize_window()

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfinDmMSxLtogWi-w20Xwy7Qumx7hhPMHl8kxAB1MpX5e2m5Q/viewform?vc=0&c=0&w=1&flr=0')
name = wait.until(EC.visibility_of_element_located(((By.XPATH , "(//input[@class='whsOnd zHQkBf'])[1]"))))
name.send_keys(" sapana gupta ")

email = wait.until(EC.visibility_of_element_located(((By.XPATH , "(//input[@class='whsOnd zHQkBf'])[2]"))))
email.send_keys("gvarsha286@gmail.com")

organization = wait.until(EC.visibility_of_element_located(((By.XPATH , "(//input[@class='whsOnd zHQkBf'])[3]"))))
organization.send_keys("sciative")

Day_of_event = wait.until(EC.visibility_of_element_located(((By.XPATH , "(//div[@class='uHMk6b fsHoPb'])[2]"))))
Day_of_event.click()

restriction = wait.until(EC.visibility_of_element_located(((By.XPATH , "(//div[@class='AB7Lab Id5V1'])[1]"))))
restriction.click()

agree = wait.until(EC.visibility_of_element_located(((By.XPATH ,"(//div[@class='uHMk6b fsHoPb'])[4]"))))
agree.click() 

submit = wait.until(EC.visibility_of_element_located(((By.XPATH , "//span[@class='l4V7wb Fxmcue']"))))
submit.click()

 
time.sleep(5)
driver.quit()