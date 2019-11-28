from modules import get_job_links, scrape_job_page, open_driver, close_driver
import os
import glob
import pandas as pd
import csv

def main():
    
    # Getting links:
    get_job_links()
    
    # Cleaning links csv:
    
    def clean_csv(path):

        print('\nCleaning: ' + path)

        with open(path, 'rt') as f:
            files = f.read().split(",")

        #, newline='\r\n'    

        files = [file.strip("\"\"") for file in files]

        page_list = []

        for file in files:
            if len(file) > 45:
                for second in file.split("\n"):
                    page_list.append(second.strip("\"\""))
            else:
                page_list.append(file)

        page_list = page_list[:-1]

        page_list = list(set(page_list))

        with open(path, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(page_list)
    
    # Cleaning linkedin_search:
    
    def clean_search(path):
        
        print('\nCleaning: ' + path)
        df = pd.read_csv(path)
        df.drop_duplicates(keep='last', inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(path, index=False)
    
    # Scraping:  
    
    how_many = '0'
    
    while how_many == '0':
    
        how_many = input('\nOne or all csv?: ')

        if how_many == 'one':
            job_title = input('\nEnter job title: ')
            job_city = input('\nEnter job location: ')
            path = "job_links/" + job_title.replace(' ', '_') + "_" + job_city.replace(' ', '_') + "_links.csv"
            clean_csv(path)
            scrape_job_page(path)
            scraped_csv = path
            
        elif how_many == 'all':
            scraped_csv = []
            for path in glob.glob('job_links/*.csv'):
                clean_csv(path)
                scrape_job_page(path)
                scraped_csv.append(path)
            
        else:
            print('Invalid input.')
            how_many = '0'

    print('\nSuccesfully scraped the following path(s): ' + str(scraped_csv))

    clean_search('linkedin_search.csv')

if __name__ == '__main__':
    main()