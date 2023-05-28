from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.maximize_window()
driver.get("https://app2.jubelio.com/login")

driver.find_element(By.NAME, "email").send_keys("bdsurel19@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Inipasswordtestnya1!")
driver.find_element(By.XPATH, "//button[text()='Masuk']").click()