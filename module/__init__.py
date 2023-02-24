import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime

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

def input_and_search(driver, licensetype_select, lastname_str):
    # Input data on fields
    select_licensetype = Select(driver.find_element(By.ID, 't_web_lookup__license_type_name'))
    select_licensetype.select_by_visible_text(licensetype_select)

    input_lastname = driver.find_element(By.ID, 't_web_lookup__last_name')
    input_lastname.send_keys(lastname_str)

    # Click search
    search_btn = driver.find_element(By.ID, 'sch_button')
    search_btn.click()

# Scrape data from one page of search result
def get_one_page_data(driver):
    '''
    input_and_search() function must run first before running this function
    driver: selenium.webdriver.Chrome() object
    returns a pandas DataFrame containing the data of the professionals
    '''
    data_dict = {
            "firstname":[],
            "middlename": [],
            "lastname": [],
            "facilityname": [],
            "license_no": [],
            "license_type": [],
            "status": [],
            "orig_issue_date": [],
            "expiry": [],
            "renewed": []
    }
    # Get all anchor tags from the results table ("datagrid_results")
    results_table_elem = driver.find_element(By.ID, "datagrid_results")
    a_tags = results_table_elem.find_elements(By.TAG_NAME, "a") # All anchor tags from the table

    # Separate names of the professionals from pagination of search results
    # Exclude the first element on a_tags list (It is a link to "License #")
    pros_indices = [a_tags.index(tag) for tag in a_tags[1:] if tag.text.isnumeric() == False]

    # Scraping in for loop iteration on results from the current page
    for i in pros_indices:
        print(f"Fetching data: index-{i}...")        
        data = a_tags[i]
        print(f"Data found:",data.text)
        data.click() # Opens a new tab
        driver.switch_to.window(driver.window_handles[1]) # Switches to the new tab
        # Fetch the data from the new tab containing the information about the professional
        data_dict['firstname'].append(driver.find_element(By.ID, '_ctl27__ctl1_first_name').text)
        data_dict['middlename'].append(driver.find_element(By.ID, '_ctl27__ctl1_m_name').text)
        data_dict['lastname'].append(driver.find_element(By.ID, '_ctl27__ctl1_last_name').text)
        data_dict['facilityname'].append(driver.find_element(By.ID, '_ctl27__ctl1_facility_name').text)
        try:
            data_dict['license_no'].append(driver.find_element(By.ID, '_ctl36__ctl1_license_no').text)
        except:
            data_dict['license_no'].append(driver.find_element(By.ID, '_ctl39__ctl1_license_no').text)
        try:
            data_dict['license_type'].append(driver.find_element(By.ID, '_ctl36__ctl1_license_type').text)
        except:
            data_dict['license_type'].append(driver.find_element(By.ID, '_ctl39__ctl1_license_type').text)
        try:
            data_dict['status'].append(driver.find_element(By.ID, '_ctl36__ctl1_status').text)
        except:
            data_dict['status'].append(driver.find_element(By.ID, '_ctl39__ctl1_status').text)
        try:
            data_dict['orig_issue_date'].append(driver.find_element(By.ID, '_ctl36__ctl1_issue_date').text)
        except:
            data_dict['orig_issue_date'].append(driver.find_element(By.ID, '_ctl39__ctl1_issue_date').text)
        try:
            data_dict['expiry'].append(driver.find_element(By.ID, '_ctl36__ctl1_expiry').text)
        except:
            data_dict['expiry'].append(driver.find_element(By.ID, '_ctl39__ctl1_expiry').text)
        try:
            data_dict['renewed'].append(driver.find_element(By.ID, '_ctl36__ctl1_last_ren').text)
        except:
            data_dict['renewed'].append(driver.find_element(By.ID, '_ctl39__ctl1_last_ren').text)

        btn_close = driver.find_element(By.NAME, "btn_close")
        btn_close.click()
        driver.switch_to.window(driver.window_handles[0])
    return pd.DataFrame(data_dict)

def generate_csv(df,prof,keyword):
    timestamp = round(datetime.now().timestamp())
    filename = f"records_{timestamp}_({prof}+{keyword}).csv"
    df.to_csv(filename,index=False)
    print(f"Generated report file: '{filename}'!")