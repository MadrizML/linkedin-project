#!/usr/bin/env python
# coding: utf-8

# In[1]:


# convert ipynb to script: $ jupyter nbconvert --to script scraping.ipynb

import time

# import web driver

from selenium import webdriver

# import keys

from selenium.webdriver.common.keys import Keys


# download ChromeDriver (and unzip): https://sites.google.com/a/chromium.org/chromedriver/downloads

wdpath = '/home/carlosmd14/LinkedIn_Project/chromedriver_linux64/chromedriver'

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(wdpath)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

time.sleep(1)


# In[2]:


# recaptcha-checkbox-border


# In[3]:


# locate email form by_class_name
username = driver.find_element_by_name('session_key')

myemail = 'carlosmadrizd@gmail.com'

# send_keys() to simulate key strokes

username.send_keys(myemail)


# In[4]:


# locate password form by_class_name
password = driver.find_element_by_name('session_password')

mypass = open('linkedin_password.txt', 'r').read()

# send_keys() to simulate key strokes
password.send_keys(mypass)


# In[5]:


# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')

# .click() to mimic button click
log_in_button.click()


# In[6]:


time.sleep(4)
# click on jobs button


# In[7]:


# locate jobs button by_class_name
jobs_button = driver.find_element_by_id('jobs-nav-item')

# .click() to mimic button click
jobs_button.click()


# In[8]:


# locate job search box
job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')

# specify job title:
time.sleep(1)
job_title = 'data analyst'

# send_keys() to simulate key strokes
job_search[0].send_keys(job_title)


# In[ ]:





# In[9]:


# locate job location box
# job_location = driver.find_element_by_class_name('jobs-search-box__text-input')

job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')


# job_search.send_keys(Keys.TAB)

# specify job title:
job_city = 'Madrid'

# send_keys() to simulate key strokes
# job_location.send_keys(job_city)
job_search[2].send_keys(job_city)


# In[10]:


# hit enter
job_search[2].send_keys(Keys.ENTER)


# In[19]:


job1 = driver.find_element_by_class_name('job-card-search__link-wrapper').get_attribute('href')[:45]

print(job1)


# In[ ]:




