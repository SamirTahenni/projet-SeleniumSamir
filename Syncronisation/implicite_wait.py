import time

from selenium import webdriver #
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.google.ca")
#time.sleep(4)    #statique
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenium")
searchgoogle= driver.find_element(By.NAME,"q")
searchgoogle.send_keys("selenium")
searchgoogle.submit()
resultlink = driver.find_element(By.XPATH,'//div[text()= "Selenium"]')
resultlink.click()
time.sleep(4)

driver.close()
