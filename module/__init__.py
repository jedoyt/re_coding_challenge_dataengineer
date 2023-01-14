import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Check Chrome browser version if match/compatible with chromedriver
def check_versions(cdriver_os):
    """
    Prints out the versions of the Chrome browser and Chrome 
    cdriver_os: (str) 'linux', 'mac', or 'win'
    Here's the link to the source of chromedrivers:
    https://chromedriver.storage.googleapis.com/index.html

    cdriver_os:
    """
    chrome_drivers = {
    'linux': "chromedriver_linux64/chromedriver",
    'mac': "chromedriver_mac64/chromedriver",
    'win': "chromedriver_win32/chromedriver.exe"
    }
    
    # Choose the right OS by changing the second argument next to 'os.getcwd()'
    driver_path = os.path.join(os.getcwd(), chrome_drivers[cdriver_os])

    # Create instance of webdriver using Chrome browser
    service = Service(executable_path = driver_path)
    driver = webdriver.Chrome(service=service)

    # Get URL
    driver.get("chrome://version/")

    # Link to source of Google Chrome Drivers
    # https://chromedriver.storage.googleapis.com/index.html

    # Version of installed Chrome Driver
    chromedriver_version = "109.0.5414.74"

    # Get version of Chrome
    chrome_ver_element = driver.find_element(By.ID, 'copy-content')
    chrome_version = str(chrome_ver_element.text).split(" ")[0]

    return  f'''
            Chrome Browser on machine:\t{chrome_version}
            Chrome Drivers installed:\t{chromedriver_version}
            Source of chromedrivers:\thttps://chromedriver.storage.googleapis.com/index.html
            '''
def set_chromedriver_os(cdriver_os='mac'):
    """
    sets the path to the right chromedriver based on the machines os
    cdriver_os: (str) 'linux', 'mac', or 'win'
    store its return value as the driver_path when creating an instance of the webdriver.Chrome()
    """
    # Choose the right OS by changing the second argument next to 'os.getcwd()'
    chrome_drivers = {
    'linux': "chromedriver_linux64/chromedriver",
    'mac': "chromedriver_mac64/chromedriver",
    'win': "chromedriver_win32/chromedriver.exe"
    }   
    return os.path.join(os.getcwd(), chrome_drivers[cdriver_os])

# Initial/placeholder storage of scraped data
data_dict = {"firstname":[],
             "middlename": [],
             "lastname": [],
             "license_no": [],
             "license_type": [],
             "status": [],
             "orig_issue_date": [],
             "expiry": [],
             "renewed": []
}

def input_and_search(driver, licensetype_select, lastname_str):
    # Input data on fields
    select_licensetype = Select(driver.find_element(By.ID, 't_web_lookup__license_type_name'))
    select_licensetype.select_by_visible_text(licensetype_select)

    input_lastname = driver.find_element(By.ID, 't_web_lookup__last_name')
    input_lastname.send_keys(lastname_str)

    # Click search
    search_btn = driver.find_element(By.ID, 'sch_button')
    search_btn.click()



# Iteration on pagination links

# Scrape data from one page
def get_one_page_data(driver):
    '''
    input_and_search() function must run first before running this function
    '''
    # Scraping in for loop iteration on results from the current page
    for i in range(3,43):
        print(f"Fetching data: {i}...")
        id = f'datagrid_results__ctl{i}_name'
        data = driver.find_element(By.ID,id)
        print(data.text)
        data.click()
        driver.switch_to.window(driver.window_handles[1])

        data_dict['firstname'].append(driver.find_element(By.ID, '_ctl27__ctl1_first_name').text)
        data_dict['middlename'].append(driver.find_element(By.ID, '_ctl27__ctl1_m_name').text)
        data_dict['lastname'].append(driver.find_element(By.ID, '_ctl27__ctl1_last_name').text)
        data_dict['license_no'].append(driver.find_element(By.ID, '_ctl36__ctl1_license_no').text)
        data_dict['license_type'].append(driver.find_element(By.ID, '_ctl36__ctl1_license_type').text)
        data_dict['status'].append(driver.find_element(By.ID, '_ctl36__ctl1_status').text)
        data_dict['orig_issue_date'].append(driver.find_element(By.ID, '_ctl36__ctl1_issue_date').text)
        data_dict['expiry'].append(driver.find_element(By.ID, '_ctl36__ctl1_expiry').text)
        data_dict['renewed'].append(driver.find_element(By.ID, '_ctl36__ctl1_last_ren').text)

        btn_close = driver.find_element(By.NAME, "btn_close")
        btn_close.click()
        driver.switch_to.window(driver.window_handles[0]) 

def generate_df_and_csv():
    data_df = pd.DataFrame(data_dict)

    print(data_df)
    data_df.to_csv("records.csv",index=False)

    return data_df