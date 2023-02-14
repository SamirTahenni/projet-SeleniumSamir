# ces commandes sont liees a l'application sous test
import time
from selenium import webdriver #
from selenium.webdriver.chrome.service import Service as ChromeService   # pour spicifier le browser
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    # en a creer un objet  de type chrome
driver.maximize_window()
driver.get("https://www.orangehrm.com")
titre_page = driver.title
print(titre_page)
Url_page = driver.current_url
print(Url_page)
code_source = driver.page_source
print(code_source)

time.sleep(4)
driver.close()

