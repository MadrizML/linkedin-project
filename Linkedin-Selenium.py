#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from parsel import Selector
import time
import numpy as np
import pandas as pd
import csv


# In[7]:


driver = webdriver.Chrome('/home/inrx/Desktop/chromedriver')


# In[8]:


page_list = [#'https://www.linkedin.com/jobs/view/1546807963/?eBP=CwEAAAFuIq0SrfWXjDtRl03XeamN43VAn2trbgH1s_a9GnVr_DugDBfxQO6-Uq63gFLUs7HFhaq6kEuragg7ZIuMp43zpCevIx-uCtEJ71fBnNnzovnJLUu08XyYbxgBEA2XAK4KInCVhd4moChaPa0d3YnB8VHMmQ1CmYu0UZZMT487D6TwuIMvbOdXl5RpsDvTZ_EXDrPfTNXl87Ap8PQ4ZtKMtTKCxu9_nN_fSKLErTMInMrJEZUMu0va96aRAxkz-FyAjvZSY3dMktWLkeq-W-shKt_cf225jpCzdssoU09JwvTKoAF-VeMZ4rDtAL9mnNRQUMgjSfyr0h_GYTmEgeeKo1oq_4eN21w1e8R0Ojl_wwDo5xq8ySCNSAji8VSXT4xAcREY8EY&recommendedFlavor=SCHOOL_RECRUIT&refId=747a511a-5ad3-435b-b846-97c19cc31a84&spSrc=CwEAAAFuIq0SzQX8rYH6OYbpb646t4U6p_vWDT4UPVGNNSsL3pGMj38Gy_tn_YBuwxiiEIpscB7opYNyIodaVN_WX_I&trk=d_flagship3_search_srp_jobs',
             #'https://www.linkedin.com/jobs/view/1509180527/?eBP=CwEAAAFuJnWlo6eGi8pZVvNFMp9C6ajzhG8sGwhVO46IIHOTIrKJO_O1ojeu4u-TedjVhgRI-CHMzRS_FlAFxP-jmTeENtxUE-Fw8LbMz3vuUX9UV-1jj9PsKwL6f2RM_26gTHj-tKOE2hSo5pTDH0NUYqnXIjN2RD306wYVt0u-EuUo6IoG9JhvRSud_JyEyU7l_7SGxKL6eJCWz4aAV2BdJPCjGOPKLDbGiIu13Xm7uB1RQXQr4B3xPoevRR8BJ52GoJOjLI7z99s2YDGVF5vUZitu2fUZwK1exI7vrsY7v2WkyJW0x-sjQ1MZnhO0qh7OftMxt_RD6-gfwCcZhSeilAbjQbIooeJsGhbrjpFmEN-B0t-VLnwWh8asEscs4zVMyY1mWv32w4dlTT3W&recommendedFlavor=IN_NETWORK&refId=a6785ac4-b32c-4002-91bf-c31c1e214f8a&spSrc=CwEAAAFuJnWlwhHXB2uqh5_LL3vRbj8cjLhdkQHIJx5Q6xpCeP8-dcRjJeB-SVVq8aBxZvCV7Uhx6B9xYl5soFOOyXI&trk=d_flagship3_search_srp_jobs',
             #'https://www.linkedin.com/jobs/view/1506504908/?eBP=CwEAAAFuJnWlo5tGBDzisPfFsoMPZ-s1VhjV1qVb5LsX0JlIQ2-XcgQYwNWPREcV39en2fYD_jtSqTiveVnkpYcqe7WqR90jR0H0xvBm4jfHYF8HmsMfw0O3K9EX9O8WksKMpKokyzccCkiFnid5ZULLUbazBf1KXoh3T-p8SM6cVk6hHbyLLYP6a05KW6avD0MmXNVzrEXCIAqontKX0PRSaBdlCkNUANSPExVaIduME4ptKkxak8njTZ8DGJCajxMR1vmFNUcdHXaj_lwx6bYOk3J50tGtv7w6FfqzGglwAoc8t0qZylpupBGSY_H4U_EYjBykxp8GZaQ6hqkcvr0neGG8lEjE6wXPic6ktiGmzyJjlE9N06geMHav9XKbcZTS0vF_IPYl2eYiSg&recommendedFlavor=IN_NETWORK&refId=a6785ac4-b32c-4002-91bf-c31c1e214f8a&spSrc=CwEAAAFuJnWlwqfUX83Q8Tk_cLuYvd0MuwyB_o2SrpsydT_Y-_85UJKmQd-p0UmPIQFLKaFt_8mZTsqQzWN5L-doax4&trk=d_flagship3_search_srp_jobs',
             #'https://www.linkedin.com/jobs/view/1446114222/?eBP=CwEAAAFuJnWloxtX3AcDZxc9EONAn7VCXprXKBv-TUjk13kgubIGcmnLwFQ8z4HtN_kLLbV15PIHbeGQmgi2c3YlMalqv-LXgZZkvXmGty0Zg4ZcfvUlHZ9xcSdPYyYxhXWRlo61gFFXuNl-19I8e-cwsfc9jTU6UpFUJY9vu5rLRsCwZz-2wpV71be8_VxdG4WxHRUvbXIm0M5So0eQescIJFX5R6Q-pQmX2Gh4-MsKSjgbY545hQD19HrtyMj9Fbj4orP_B54CBeO51jfnjz28PPJyK-LNWtujt16apvcn9jHJBSqPrO5IJauWVOYC7Sb6z8dTkI0vFmirOO1GlG1urIrNVE69aW4e1Nlz10yT0qqMT5TptEBX78Hr97mTFOS1lU6OxrO9yBUOYlb2&recommendedFlavor=IN_NETWORK&refId=a6785ac4-b32c-4002-91bf-c31c1e214f8a&spSrc=CwEAAAFuJnWlwgyoraGFfIZpJVljuWZQ2A9dU6-G9awstKgbqDKrbZq7E5Hkj_BMtio9GFlQzwuL0rgleBqVglaR72g&trk=d_flagship3_search_srp_jobs',
             #'https://www.linkedin.com/jobs/view/1566818580/?eBP=NotAvailableFromVoyagerAPI&recommendedFlavor=SCHOOL_RECRUIT&refId=a6785ac4-b32c-4002-91bf-c31c1e214f8a&trk=d_flagship3_search_srp_jobs',
             #'https://www.linkedin.com/jobs/view/1538163636/?eBP=NotAvailableFromVoyagerAPI&recommendedFlavor=IN_NETWORK&refId=a6785ac4-b32c-4002-91bf-c31c1e214f8a&trk=d_flagship3_search_srp_jobs'
            ]


# In[9]:


page_list = ['https://www.linkedin.com/jobs/view/1526861678/',
            'https://www.linkedin.com/jobs/view/1538168934/',
            'https://www.linkedin.com/jobs/view/1585144716/',
            'https://www.linkedin.com/jobs/view/1579616329/',
            'https://www.linkedin.com/jobs/view/1506528365/',
            'https://www.linkedin.com/jobs/view/1520663107/',
            'https://www.linkedin.com/jobs/view/1541346509/'
            ]


# In[10]:


# import libraries
from selenium import webdriver
from parsel import Selector
import time
import numpy as np
import pandas as pd
import csv

# Create for loop to scrap data from job posting pages
for page in page_list:
    job_path = page
    driver.get(job_path)
    
    # sleep to avoid crawler detection
    time.sleep(2)

    # click "see more" to retrieve all the information from the job posting 
    see_more = driver.find_element_by_xpath("//button[@data-control-name='see_more']")
    see_more.click()
    
    # sleep to avoid crawler detection
    time.sleep(1)

    # scrap job title
    job_title = driver.find_element_by_class_name('jobs-top-card__job-title')
    job_title_final = job_title.text
    
    # scrap company name 
    company_raw = driver.find_element_by_class_name('jobs-top-card__company-url')
    company_final = company_raw.text

    # scrap company link
    company_link_raw = driver.find_element_by_class_name("jobs-top-card__company-url")
    company_link_final = company_link_raw.get_attribute('href')

    # scrap number of applicants and post date
    applications_raw = driver.find_elements_by_xpath("//p[@class='mt1 full-width flex-grow-1 t-14 t-black--light']")
    applications_final = [x.text for x in applications_raw]
    ## obtain only the post date and number of applicant, since the date retrieve has all the information
    applications_final_split = [x.split('\n') for x in applications_final][0]
    ### obtain post date and number of applicants
    post_date, applications = applications_final_split[1],applications_final_split[3]
    
    # Srap the full description of the job
    role = driver.find_element_by_class_name("jobs-description__container")
    role_final = role.text

    # Since the information changes from page to page we create a try except rule
    ## Scrap Location
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
           job_poster_link_final]
    
    time.sleep(2)
    
    # Append each row in the end of the existing .csv file
    with open('linkedin_search.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(row)
    


# In[ ]:




