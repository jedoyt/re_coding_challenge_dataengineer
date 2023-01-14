import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import pandas as pd

# driver paths
linux = "chromedriver_linux64/chromedriver"
mac = "chromedriver_mac64/chromedriver"
win = "chromedriver_win32/chromedriver.exe"

# Choose the right OS by changing the second argument next to 'os.getcwd()'
driver_path = os.path.join(os.getcwd(), mac)

# Create instance of webdriver using Chrome browser
service = Service(executable_path = driver_path)
driver = webdriver.Chrome(service=service)

# Get URL
driver.get("https://idbop.mylicense.com/verification/Search.aspx")

# Field Inputs
licensetype_select = "Pharmacist"
lastname_str = "L"

# Input data on fields
select_licensetype = Select(driver.find_element(By.ID, 't_web_lookup__license_type_name'))
select_licensetype.select_by_visible_text(licensetype_select)

input_lastname = driver.find_element(By.ID, 't_web_lookup__last_name')
input_lastname.send_keys(lastname_str)

# Click search
search_btn = driver.find_element(By.ID, 'sch_button')
search_btn.click()

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

# Iteration on pagination links

# Scraping in for loop iteration
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

data_df = pd.DataFrame(data_dict)

print(data_df)
data_df.to_csv("records.csv",index=False)

driver.quit()