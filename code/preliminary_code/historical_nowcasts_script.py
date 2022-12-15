###
### Scrape historical nowcasts to local file
###

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium import webdriver as wd
from time import sleep
import pandas as pd
import datetime
import glob
import os
os.chdir('Downloads')

# Navigate to main page

driver = wd.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
url = 'https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting'
driver.get(url)

# Select the section for monthly, year-over-year observations

monthly_yoy_id = 'section-title-3-19'
monthly_yoy = driver.find_element(by='id', value=monthly_yoy_id)
monthly_yoy.click()

# Now there will be a dropdown menu with Year:Month pairs
# Create a Selenium Select object of the menu

menu_id = 'menu_year'
menu = driver.find_element(by='id', value=menu_id)
select = Select(menu)
selections = select.options

# Each Year:Month pair displays allows CSV download
# Loop through all time periods and download CSVs
# Clean and merge to master file

# Note that I skip index 0, '2013-7'
# because forecasts begin from index 1
# upon manual inspection

for i in range(1, len(selections)):
    select.select_by_index(i)
    
    # Download CSV file of historical nowcasts for Year:Month pair
    
    csv_download_id = 'btn-NowcastDownload-year'
    csv_download = driver.find_element(by='id', value=csv_download_id)
    csv_download.click()
    sleep(1)
    
    # Clean and format historical nowcasts for Year:month pair
    
    files = glob.glob(os.getcwd() + '\*.csv')
    recent_file = max(files, key=os.path.getctime)
    df_current = pd.read_csv(recent_file)
    df_current.dropna(inplace=True)
    
    # Subset the data to include only observations
    # as of relevant month
    
    # Include tag for last day of month in series
    # as this is not always actual last day of month
    
    dt_date = datetime.datetime.strptime(selections[i].text, '%Y-%m')
    check_datestring = selections[i].text.split('-')[-1].zfill(2)
    date_mask = df_current['Label'].str.startswith(check_datestring)
    df_current = df_current[date_mask]
    df_current['is_last_day'] = 0
    df_current['is_last_day'].iloc[-1] = 1
    df_current['day'] = df_current['Label'].str.split('/').str[-1].astype(int)
    df_current['month'] = dt_date.month
    df_current['year'] = dt_date.year
    df_current['date'] = pd.to_datetime(df_current[['year', 'month', 'day']])
    df_current['year-month'] = df_current['year'].astype(str) + '-' + df_current['month'].astype(str)
    
    # Append to master file
    df_current.to_csv('historical_nowcasts.csv', mode='a', header=False, index=False)

driver.quit()