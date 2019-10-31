#!/usr/bin/env python
# coding: utf-8

# In[43]:


# convert ipynb to script: $ jupyter nbconvert --to script scraping.ipynb

import time

# import web driver
from selenium import webdriver

# download ChromeDriver (and unzip): https://sites.google.com/a/chromium.org/chromedriver/downloads

wdpath = '/home/carlosmd14/Documents/LinkedIn_Project/chromedriver_linux64/chromedriver'

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(wdpath)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

time.sleep(1)


# In[32]:


# locate email form by_class_name
username = driver.find_element_by_name('session_key')


# In[33]:


myemail = 'carlosmadrizd@gmail.com'

# send_keys() to simulate key strokes

username.send_keys(myemail)


# In[34]:


# locate password form by_class_name
password = driver.find_element_by_name('session_password')


# In[35]:


mypass = open('linkedin_password.txt', 'r').read()

# send_keys() to simulate key strokes
password.send_keys(mypass)


# In[36]:


# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')


# In[37]:


# .click() to mimic button click
log_in_button.click()


# In[ ]:


time.sleep(4)
# click on jobs button


# In[ ]:


# locate jobs button by_class_name
jobs_button = driver.find_element_by_id('jobs-nav-item')


# In[ ]:


# .click() to mimic button click
jobs_button.click()


# In[ ]:




