#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
from selenium import webdriver
from parsel import Selector
import time
import numpy as np
import pandas as pd
import csv
import random


# In[2]:


driver = webdriver.Chrome('/home/inrx/Desktop/chromedriver')


# In[3]:


path = '/home/inrx/Ironhack/TA/job-search/linkedin-project/data analyst_links.csv'

with open(path, 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

page_list_raw = your_list[0]
page_list = page_list_raw[1:10]


# In[4]:


# Create for loop to scrap data from job posting pages
number = 0

for page in page_list:
    job_path = page
    driver.get(job_path)

    # sleep to avoid crawler detection
    time.sleep(round(random.uniform(12,15), 2))
    try:
        # click "see more" to retrieve all the information from the job posting 
        see_more = driver.find_element_by_xpath("//button[@data-control-name='see_more']")
        see_more.click()

        # sleep to avoid crawler detection
        time.sleep(round(random.uniform(2,5), 2))

        # scrap job title
        job_title = driver.find_element_by_class_name('jobs-top-card__job-title')
        job_title_final = job_title.text

        # scrap company name 
        try:
            company_raw = driver.find_element_by_class_name('jobs-top-card__company-url')
            company_final = company_raw.text

        except:
            company_raw = driver.find_elements_by_class_name('jobs-top-card__company-info')
            company = [x.text for x in company_raw]
            company_final = [x.split('\n') for x in company][0][1]
            location_final = [x.split('\n') for x in company][0][3]

        # scrap company link
        try:
            company_link_raw = driver.find_element_by_class_name("jobs-top-card__company-url")
            company_link_final = company_link_raw.get_attribute('href')
        except:
            company_link_final = np.NaN

        # scrap number of applicants and post date
        applications_raw = driver.find_elements_by_xpath("//p[@class='mt1 full-width flex-grow-1 t-14 t-black--light']")
        applications_final = [x.text for x in applications_raw]
        ## obtain only the post date and number of applicant, since the date retrieve has all the information
        applications_final_split = [x.split('\n') for x in applications_final][0]
        ### obtain post date and number of applicants
        post_date, applications = applications_final_split[1],applications_final_split[3]

        # Srap the full description of the job
        role = driver.find_element_by_class_name("jobs-box__html-content")
        role_final = role.text

        # Since the information changes from page to page we create a try except rule
        ## Scrap Location
        if location_final == '':
            try:
                location_raw = driver.find_element_by_xpath("//span[@class='jobs-top-card__bullet']")
                location_final = location_raw.text
            except:
                location_raw = driver.find_elements_by_class_name("jobs-top-card__bullet")
                location_final = [x.text for x in location_raw][0]


        ## Scrap skills
        try:
            skills = driver.find_element_by_xpath("//ul[@class='jobs-ppc-criteria__list jobs-ppc-criteria__list--skills jobs-ppc-criteria__list--is-last js-criteria-skills list-style-none']")
            skills_final = skills.text
        except:
            ## If non existant fill with NaN
            skills_final = np.NaN


        ## Scrap job poster and link
        try:
            job_poster = driver.find_element_by_class_name("jobs-poster__name")
            job_poster_final = job_poster.text
            job_poster_link = driver.find_element_by_xpath("//a[@data-control-name='jobdetails_profile_poster']")
            job_poster_link_final = job_poster_link.get_attribute('href')
        except:
            ## If non existant fill with NaN
            job_poster_final = np.NaN
            job_poster_link_final = np.NaN

        # Create a row with all the scrapped info to append to the .csv file
        row = [job_title_final, 
               company_final, 
               company_link_final, 
               post_date, 
               applications, 
               location_final, 
               skills_final, 
               role_final, 
               job_poster_final, 
               job_poster_link_final,
               job_path]


        # Append each row in the end of the existing .csv file
        with open('linkedin_search.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(row)
    except:
        pass

#    number += 1
#    print (number)


# In[ ]:




