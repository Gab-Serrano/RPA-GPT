from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# Apunta al chromedriver.exe (asegúrate de que sea compatible con tu versión de Chrome)
service = ChromeService()

driver = webdriver.Chrome(options=options)
driver.get("https://chat.openai.com/")

# Wait for ChatGPT to respond
time.sleep(5)

login_button = driver.find_element(By.XPATH, "//button[@data-testid='login-button']")
login_button.click()
time.sleep(60)

input_user = driver.find_element(By.XPATH, "//input[@name='username']")
input_user.send_keys('gab.serrano@duocuc.cl')
input_user.send_keys(Keys.ENTER)
time.sleep(10)

input_user = driver.find_element(By.XPATH, "//input[@name='password']")
input_user.send_keys('Iwtltpuyam123')
input_user.send_keys(Keys.ENTER)
time.sleep(5)

pop_up = driver.find_element(By.XPATH, "//div[text(), 'Okay, let’s go']")
pop_up.click()
time.sleep(5)

input_field = driver.find_element(By.CSS_SELECTOR,"#prompt-textarea")

input_field.send_keys('What is the capital of France?')
input_field.send_keys(Keys.ENTER)

turn = 3
reponse_xpath = "//div[@data-testid='conversation-turn-'", str(turn), "]"
response = driver.find_element(By.XPATH, reponse_xpath)
print(response.text)

time.sleep(5)