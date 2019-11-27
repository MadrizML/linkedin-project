import pandas as pd
import glob

def clean_csv(path):
    print('Cleaning: ' + path)
    df = pd.read_csv(path)
    df.drop_duplicates(keep='last', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(path, index=False)

for path in glob.glob('job_links/*.csv'):
    clean_csv(path)

path = 'linkedin_search.csv'
    
clean_csv(path)