import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)

list_link =driver.find_elements(By.TAG_NAME,"a")
compteur =0
for link in list_link:
    URL = link.get_attribute("href")
    try:
     response = requests.head(URL)
    except:
        None
    if response.status_code>=400:
        print(URL,"est un liens brisé")
        compteur=compteur+1
    else:
        print(URL,"est un liens valide")
print("le nombre de liens brisés est :",compteur)




driver.close()