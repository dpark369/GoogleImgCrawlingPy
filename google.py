from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from urllib.request import urlretrieve

driver = webdriver.Chrome()
driver.get("https://images.google.com/")
elem = driver.find_element_by_name("q")
elem.send_keys("test") #Selects what to search
elem.send_keys(Keys.RETURN) #Presses Enter in the Search Bar



# Scrolls down webpage
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0
for image in images: 
    try:
        image.click()
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
        time.sleep(1)    
        urlretrieve(imgUrl, str(count)+ ".jpg")
        count +=  1
    except:
        pass





# assert "No results found." not in driver.page_source
driver.close()