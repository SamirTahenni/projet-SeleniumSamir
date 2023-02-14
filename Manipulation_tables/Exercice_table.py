import time

from selenium import webdriver #
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By      # loclaisation des elements
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
driver.find_element(By.XPATH,'//span[text()= "Admin"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//span [text()="User Management "]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//a [@role="menuitem"]').click()
time.sleep(3)
Nombre_ligne= driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(Nombre_ligne))