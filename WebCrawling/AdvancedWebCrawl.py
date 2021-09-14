#this scrolls to the end
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp?hl=en&ogbl")

#find which one to use by pressing f12 and then inspect element
elem = driver.find_element_by_name("q") #search bar
elem.send_keys("Apple") #send what to type on the search bar
elem.send_keys(Keys.RETURN) #press enter

SCROLL_PAUSE_TIME = 1

#find height of browser with javascript and store in last_height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to all the way to end of browser height
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    #this means you can't scroll anymore since it's the end of the results
    if new_height == last_height:
    #now we gotta click on "Show more results" to view more images
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height


#if you dont want to download all the images but just want to scroll to the end
#please comment the code below

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
#above selects all the preview images and stores them in a list
count = 1
for image in images:
    try:
        image.click() #click on image to get to "big" image part
        time.sleep(2) #this ensures code waits till it gets to the image and then gets the src
        #gets to the "big" image part and then gets url of the image to download + storing address to imgUrl
        #i copied the full xpath for it to be more precise
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass


driver.close() #closes browser
