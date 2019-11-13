#!/usr/bin/env python
# coding: utf-8


# import libraries
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.chrome.options import Options


def open_driver():

    print('Opening driver')
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    if input('Headless? (Y/n): ').lower() == 'n':
        driver = webdriver.Chrome()  
    else:
        driver = webdriver.Chrome(options=chrome_options)
        
        
def close_driver():
    
    print('\nClosing driver')
    driver.quit()