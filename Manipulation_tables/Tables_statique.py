import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
#Recuperation le nombre de lignes et colonnes d'une table
Nombre_ligne= driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(Nombre_ligne))
Nombre_Colonne=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(Nombre_Colonne))
# Recupere la valeur d'une cellule
Valeur_cellule =driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[2]/td[1]")
print(Valeur_cellule)
#Recuperer toutes les donnes du tableau
Nombre_ligne=len( driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
Nombre_Colonne= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))

valeur_head = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
for i in range(1,len(valeur_head)+1):
    data_head = driver.find_element(By.XPATH, "//table[@name='BookTable']//th["+str(i)+"]").text
    print(data_head)

time.sleep(4)
for r in range(2,Nombre_ligne+1):
    for c in range(1,Nombre_Colonne+1):
        Valeur_cellule = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
       #Val_cell= driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(Valeur_cellule,end="        ")
    print()

# Recuperer tous les livre ecrit part amit et leur prix
for r in range(2,Nombre_ligne+1):
    auteur = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text


    if auteur == 'Amit':
        prix = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        Nom_livre = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        print(auteur,"******",Nom_livre,"********",prix)




driver.close()