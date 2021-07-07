from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from urllib.request import urlretrieve
import os

search = "test" #Select what to Search
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, search)        #Makes new directory of the search name
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

#Goes to website

driver = webdriver.Chrome()
driver.get("https://images.google.com/")
elem = driver.find_element_by_name("q")
elem.send_keys(search) 
elem.send_keys(Keys.RETURN) #Presses Enter in the Search Bar



# Scrolls down webpage and clicks load more

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

#Clicks and downloads each Image

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0
for image in images: 
    try:
        image.click()
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
        time.sleep(1)    
        fullfilename = os.path.join(final_directory, str(count)+ ".jpg")
        urlretrieve(imgUrl, fullfilename)
        count +=  1
    except:
        pass



# Closes after finishing the task
driver.close()