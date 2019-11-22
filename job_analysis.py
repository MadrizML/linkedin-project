from modules import get_job_links, scrape_job_page, open_driver, close_driver
import os
import glob

def main():
    
    # Getting links:
    get_job_links()
    
    # Scraping:   
    how_many = '0'
    
    while how_many == '0':
    
        how_many = input('\nOne or all csv?: ')

        if how_many == 'one':
            job_title = input('\nEnter job title: ')
            job_city = input('\nEnter job location: ')
            path = "job_links/" + job_title.replace(' ', '_') + "_" + job_city.replace(' ', '_') + "_links.csv"
            scrape_job_page(path)
            scraped_csv = path
            
        elif how_many == 'all':
            scraped_csv = []
            for path in glob.glob('job_links/*.csv'):
                scrape_job_page(path)
                scraped_csv.append(path)
            
        else:
            print('Invalid input.')
            how_many = '0'

    print('\nSuccesfully scraped the following path(s): ' + str(scraped_csv))

    

if __name__ == '__main__':
    main()