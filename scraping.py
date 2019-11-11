#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# imports:

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
import csv


# In[ ]:


# download ChromeDriver (and unzip): https://sites.google.com/a/chromium.org/chromedriver/downloads


wdpath = input("Enter chromedriver's path: ") or '/home/carlosmd14/LinkedIn_Project/chromedriver_linux64/chromedriver'


# specifies the path to the chromedriver executable file
driver = webdriver.Chrome(wdpath)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

time.sleep(1)


# In[ ]:


# recaptcha-checkbox-border


# In[ ]:


# locate email form by_class_name
username = driver.find_element_by_name('session_key')

my_email = input('Enter your email: ') or 'carlosmadrizd@gmail.com'

# send_keys() to simulate key strokes

username.send_keys(my_email)


# In[ ]:


# locate password form by_class_name
password = driver.find_element_by_name('session_password')

mypass = getpass('Enter your password: ') or open('linkedin_password.txt', 'r').read()

# send_keys() to simulate key strokes
password.send_keys(mypass)


# In[ ]:


# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')

# .click() to mimic button click
log_in_button.click()


# In[ ]:


time.sleep(2)
# click on jobs button


# In[ ]:


# locate jobs button by_class_name
jobs_button = driver.find_element_by_id('jobs-nav-item')

# .click() to mimic button click
jobs_button.click()


# In[ ]:


# locate job search box
job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')

# specify job title:
time.sleep(1)
job_title = input('Enter job title: ').replace(" ", "_") or 'data_analyst'

# send_keys() to simulate key strokes
job_search[0].send_keys(job_title)


# In[ ]:


# locate job location box
# job_location = driver.find_element_by_class_name('jobs-search-box__text-input')

job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')


# job_search.send_keys(Keys.TAB)

# specify job title:
job_city = input('Enter location: ') or 'Madrid'

# send_keys() to simulate key strokes
# job_location.send_keys(job_city)
job_search[2].send_keys(job_city)


# In[ ]:


# hit enter
job_search[2].send_keys(Keys.ENTER)


# In[ ]:


time.sleep(3)


# In[ ]:


# Hover

# element_to_hover_over = driver.find_element_by_class_name('job-card-search__link-wrapper')

# hover = ActionChains(driver).move_to_element(element_to_hover_over)
# hover.perform()


# In[ ]:


i = 0
while i<20:
    scroll = driver.find_element_by_class_name('job-card-search__link-wrapper').send_keys(Keys.END)
    time.sleep(1)
    i+=1


# In[ ]:


jobs_raw = driver.find_elements_by_class_name('job-card-search__link-wrapper')

job_links = list(set([job.get_attribute('href')[:45] for job in jobs_raw]))


# In[ ]:


print(f"You scraped {len(job_links)} {job_title.replace('_', ' ')} job links in {job_city}. "       f"It\'s gonna be stored in {job_title}_links.txt")


# In[ ]:


with open(job_title + "_links.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(job_links)


# In[ ]:


# jupyter nbconvert --to script scraping.ipynb

