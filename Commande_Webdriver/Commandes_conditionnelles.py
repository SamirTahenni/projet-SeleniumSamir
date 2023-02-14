import time

from selenium import webdriver #
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(4)
check_selected_element = driver.find_element(By.ID,'checkbox2').is_selected()  #Vérifier l’élément sélectionné
time.sleep(3)
print(check_selected_element)
time.sleep(3)
check_enabled_element = driver.find_element(By.ID,'but1').is_enabled()   #Vérifier l’élément activé
time.sleep(3)
print(check_enabled_element)
check_displayed_element = driver.find_element(By.ID,'hbutton').is_displayed()   #Vérifier l’élément affiché
time.sleep(3)
print(check_displayed_element)

driver.close()
