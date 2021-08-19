from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


driver = webdriver.Chrome('C:/Users/cd/chromedriver.exe')

# open the webpage
driver.get("http://www.instagram.com")

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys("vintage.fashion_styleofny")
password.clear()
password.send_keys("fahim@dummy")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()




# Add exceptions
try:
    not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
except:
    pass
try:
    not_now2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
except:
    pass



import time

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

keyword = "#russiangirlsgram"
searchbox.send_keys(keyword)

time.sleep(10)

driver.execute_script("window.scrollTo(0, 4000);")
time.sleep(10)

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

print('Number of scraped images: ', len(images))

# In[17]:


import os
import wget

path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

os.mkdir(path)

# In[18]:


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1






