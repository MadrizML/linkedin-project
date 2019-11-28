#!/usr/bin/env python
# coding: utf-8


# import libraries
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import pandas as pd
import csv
import random
import re
from tqdm import tqdm
from tqdm import tqdm_gui


    #path = 'job_links/data_analyst_European_Economic_Area_links.csv'

    
def scrape_job_page(path):
    
    print('\nOpening driver')
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    if input('\nHeadless? (Y/n): ').lower() == 'n':
        driver = webdriver.Chrome()  
    else:
        driver = webdriver.Chrome(options=chrome_options)
    
    with open(path, 'r') as f:
        reader = csv.reader(f)
        page_list = list(reader)

    page_list = [a for sub in page_list for a in sub]
    
    
    # Create for loop to scrap data from job posting pages
    number = 0

    for page in tqdm(page_list, desc='Scraping links from ' + path, ncols=80 ,position=0):
        job_path = page
        driver.get(job_path)

        # sleep to avoid crawler detection
        time.sleep(round(random.uniform(1,1.5), 2))

        # scrap job title
        job_title = driver.find_element_by_class_name('topcard__title')
        job_title_final = job_title.text
        # topcard__title

        # scrap company name 
        try:
            company_raw = driver.find_element_by_class_name('topcard__org-name-link')
            company_final = company_raw.text
        except: #topcard__flavor
            company_raw = driver.find_element_by_class_name('topcard__flavor')
            company_final = company_raw.text
        #location_final = ''

        # scrap company link
        try:
            company_link_raw = driver.find_element_by_class_name("topcard__org-name-link")
            company_link_final = company_link_raw.get_attribute('href')
        except:
            company_link_final = np.NaN


        # scrap number of applicants and post date
        applications_raw = driver.find_element_by_class_name("num-applicants__caption")
        applications_final = applications_raw.text
        if applications_final == 'Seja um dos 25 primeiros candidatos' or applications_final == 'Be among the first 25 applicants':
            applications_final = '<25'


        ### obtain post date and number of applicants
        post_date_raw = driver.find_element_by_class_name('topcard__flavor--metadata')
        post_date = post_date_raw.text

        # Srap the full description of the job
        role = driver.find_element_by_class_name("description__text")
        role_final = role.text


        ## Scrap Location
        location_raw = driver.find_element_by_xpath("//span[@class='topcard__flavor topcard__flavor--bullet']")
        location_final = location_raw.text


        ## Scrap job critera
        criteria_raw = driver.find_elements_by_class_name('job-criteria__list')
        criteria = [x.text for x in criteria_raw]
        criteria_1 = [x.split('\n') for x in criteria]
        ### Scrap seniority level
        experience = criteria_1[0][1]
        ### Scrap type of contract
        type_work = criteria_1[0][3]
        ### Scrap the function type
        function = criteria_1[0][5]
        ### Scrap the sector of the company
        sector = criteria_1[0][7]
        sector_final = sector


        # Create a row with all the scrapped info to append to the .csv file
        row = [job_title_final, 
               company_final, 
               company_link_final, 
               post_date, 
               applications_final, 
               location_final, 
               role_final, 
               job_path,
               experience,
               type_work,
               function,
               sector_final]


        # Append each row in the end of the existing .csv file
        with open('linkedin_search.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(row)
            number += 1

    print('\nDone.')
    
    print('\nClosing driver')
    driver.quit()

