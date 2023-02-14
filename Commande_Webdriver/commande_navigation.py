import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://www.orangehrm.com")
time.sleep(4)
driver.get("https://www.google.ca")
time.sleep(4)
driver.back()
time.sleep(3)
driver.forward()              # represente les deux fleche avant arriere et refrech
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.close()