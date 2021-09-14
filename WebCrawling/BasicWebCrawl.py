#this is only for the firstly loaded images so basically 50
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

#selects all the preview images and stores them in a list
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click() #click on image to get to "big" image part
        time.sleep(3) #this ensures code waits till it gets to the image and then gets the src
        #gets to the "big" image part and then gets url of the image to download + storing address to imgUrl
        #i copied the full xpath for it to be more precise
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        #download image from url and save as
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:  #if error occurs just move on
        pass

driver.close()
