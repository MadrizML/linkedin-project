#!/usr/bin/env python
# coding: utf-8


# import libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from getpass import getpass
import csv
from tqdm import tqdm


def get_job_links():


    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    if input('Headless? (Y/n): ').lower() == 'n':
        driver = webdriver.Chrome()  
    else:
        driver = webdriver.Chrome(options=chrome_options)

    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.linkedin.com')

    time.sleep(1)

    # recaptcha-checkbox-border

    # locate email form by_class_name
    username = driver.find_element_by_name('session_key')

    # my_email = input('Enter your email: ') or 'carlosmadrizd@gmail.com'

    my_email = input('Email (i for Inês and c for Carlos): ')
    
    if my_email == 'c':
        
        my_email = 'carlosmadrizd@gmail.com'
        
        
    elif my_email == 'i':
        
        my_email = 'ines.garcia263@gmail.com'

    # send_keys() to simulate key strokes

    username.send_keys(my_email)

    # locate password form by_class_name
    password = driver.find_element_by_name('session_password')

    try:
        
        mypass = open('linkedin_password.txt', 'r').read()
    
    except:
        
        mypass = getpass('\nEnter your password: ')
    

    # send_keys() to simulate key strokes
    password.send_keys(mypass)

    # locate submit button by_class_name
    log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')

    # .click() to mimic button click
    log_in_button.click()

    print('\nLogging in...')
    
    time.sleep(2)
    # click on jobs button

    # locate jobs button by_class_name
    jobs_button = driver.find_element_by_id('jobs-nav-item')

    # .click() to mimic button click
    jobs_button.click()
    

    # locate job search box
    job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')

    # specify job title:
    
    print('\nJobs page loading...')
    time.sleep(1)
    job_title = input('\nEnter job title (default is data_scientist): ').replace(" ", "_") or 'data_scientist'

    # send_keys() to simulate key strokes
    job_search[0].send_keys(job_title)


    # locate job location box

    job_search = driver.find_elements_by_class_name('jobs-search-box__text-input')


    # job_search.send_keys(Keys.TAB)

    # specify job title:
    job_city = input('\nEnter location (default is European Economic Area): ') or 'European Economic Area'

    # clear existing string:
    job_search[2].clear()
    
    # send_keys() to simulate key strokes
    job_search[2].send_keys(job_city)

    # hit enter
    job_search[2].send_keys(Keys.ENTER)

    print('\nLoading jobs...')
    
    time.sleep(3)

    try:
        scroll_limit = int(input('\nScroll limit (default is 65): '))
    except:
        scroll_limit = 65

    for i in tqdm(range(scroll_limit), desc='Scrolling down...', ncols=100, position=0, leave=True):
        
        driver.find_element_by_class_name('job-card-search__link-wrapper').send_keys(Keys.END)
        time.sleep(1)

    jobs_raw = driver.find_elements_by_class_name('job-card-search__link-wrapper')

    job_links = list(set([job.get_attribute('href')[:45] for job in jobs_raw]))

    print(f"You scraped {len(job_links)} {job_title.replace('_', ' ')} job links in {job_city}. "           f"It\'s gonna be stored in {job_title}_links.csv")

    with open("job_links/" + job_title.replace(' ', '_') + "_" + job_city.replace(' ', '_') + "_links.csv", 'w', newline='') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(job_links)

    driver.quit()
