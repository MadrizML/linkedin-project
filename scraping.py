#!/usr/bin/env python
# coding: utf-8

# In[104]:


# imports:

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# In[105]:


# download ChromeDriver (and unzip): https://sites.google.com/a/chromium.org/chromedriver/downloads


wdpath = input("Enter chromedriver's path: ") or '/home/carlosmd14/LinkedIn_Project/chromedriver_linux64/chromedriver'
    

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(wdpath)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

time.sleep(1)


# In[106]:


# recaptcha-checkbox-border


# In[107]:


# locate email form by_class_name
username = driver.find_element_by_name('session_key')

my_email = input('Enter your email: ') or 'carlosmadrizd@gmail.com'

# send_keys() to simulate key strokes

username.send_keys(my_email)


# In[108]:


# locate password form by_class_name
password = driver.find_element_by_name('session_password')

mypass = input('Enter your password: ') or open('linkedin_password.txt', 'r').read()

# send_keys() to simulate key strokes
password.send_keys(mypass)


# In[109]:


# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')

# .click() to mimic button click
log_in_button.click()


# In[110]:


time.sleep(2)
# click on jobs button


# In[111]:


# locate jobs button by_class_name
jobs_button = driver.find_element_by_id('jobs-nav-item')

# .click() to mimic button click
jobs_button.click()


# In[112]:


# locate job search box
job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')

# specify job title:
time.sleep(1)
job_title = input('Enter job title: ') or 'data analyst'

# send_keys() to simulate key strokes
job_search[0].send_keys(job_title)


# In[113]:


# locate job location box
# job_location = driver.find_element_by_class_name('jobs-search-box__text-input')

job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')


# job_search.send_keys(Keys.TAB)

# specify job title:
job_city = input('Enter location: ') or 'Madrid'

# send_keys() to simulate key strokes
# job_location.send_keys(job_city)
job_search[2].send_keys(job_city)


# In[114]:


# hit enter
job_search[2].send_keys(Keys.ENTER)


# In[115]:


time.sleep(2)


# In[116]:


# Hover

# element_to_hover_over = driver.find_element_by_class_name('job-card-search__link-wrapper')

# hover = ActionChains(driver).move_to_element(element_to_hover_over)
# hover.perform()


# In[117]:


i = 0
while i<15:
    scroll = driver.find_element_by_class_name('job-card-search__link-wrapper').send_keys(Keys.END)
    time.sleep(1)
    i+=1


# In[118]:


jobs_raw = driver.find_elements_by_class_name('job-card-search__link-wrapper')

job_links = list(set([job.get_attribute('href')[:45] for job in jobs_raw]))


# In[122]:


print(f"You scraped {len(job_links)} job links.")


# In[120]:


with open("job_links.txt", "w") as output:
    output.write(str(job_links))


# In[ ]:




