import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(4)
driver.switch_to.frame("packageListFrame")
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href ='org/openqa/selenium/package-frame.html']").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
time.sleep(2)
driver.find_element(By.XPATH,"//span[text() ='WebDriver']").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
#driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe')[2])
time.sleep(2)
driver.find_element(By.XPATH,"(//a[text() ='Help'])[1]").click()
time.sleep(2)

