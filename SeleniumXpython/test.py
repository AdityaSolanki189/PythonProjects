from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#access the website and print the title of the website
driver.get("https://techwithtim.net")
print(driver.title)

#finding the search box and searching 'test'
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

#wait for the main to load and print the articles
try:
    main = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
    
finally:
    driver.quit()

