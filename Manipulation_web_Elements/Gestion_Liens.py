import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
list_link =driver.find_elements(By.TAG_NAME,"a")           #recupere le nombre de liens existe sur le site
print("le nombre de liens sur la page est :",len(list_link))

for link in list_link:                            #Affiche tout les liens existe sur le site
    print(link.text)
    print(link.get_attribute("href"))

driver.close()