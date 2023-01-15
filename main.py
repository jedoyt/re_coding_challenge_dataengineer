from module import *

# I. INPUT PREFERENCES
# Set machine's os: 'linux', 'mac', 'win'
machine_os = 'mac'

# Field Inputs
licensetype_select = "Pharmacist"
lastname_str = "A"
# Other License options: 'All', 'Certified Pharmacy Technician', 'Intern - Graduate', 'Intern - Student',
# 'Non-Resident Pharmacist', 'Non-Resident PIC', 'Pharmacist', 'Pharmacy Technician', 'Pharmacy Technician in Training', 
# 'Practitioner Controlled Substance', 'Researcher Controlled Substance', 'Student Pharmacy Technician'

# II. CHECK VERSIONS
# Check versions of chrome browser and chrome drivers
print(check_versions(machine_os))

# III. SETUP WEBDRIVER
driver_path = set_chromedriver_os(machine_os) # Setup driver path, select the machine's os

# Create instance of webdriver using Chrome browser
service = Service(executable_path = driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://idbop.mylicense.com/verification/Search.aspx") # Get URL

# IV. WEB AUTOMATION AND SCRAPING
# Enter field inputs and click search
input_and_search(driver, licensetype_select, lastname_str)

#results_table_elem = driver.find_element(By.ID, "datagrid_results")
a_tags = driver.find_element(By.ID, "datagrid_results").find_elements(By.TAG_NAME, "a")

# Separate names of the professionals from page nums of search results
pros_indices = [a_tags.index(tag) for tag in a_tags[1:] if tag.text.isnumeric() == False]
pagination_indices = [a_tags.index(tag) for tag in a_tags if tag.text.isnumeric()]

page_link_elems = [tag for tag in a_tags if tag.text.isnumeric()]

print("No. of '<a>' tags:",len(a_tags))
print("No. of Professionals:", len(pros_indices))
print("No. of page results:", len(pagination_indices))
print("Professionals:",pros_indices)
print("Pagination indices:",pagination_indices)
print("Page Result Links:", [elem.text for elem in page_link_elems])

# Create initial DataFrame and csv file
data_dict = {"firstname":[],
                "middlename": [],
                "lastname": [],
                "license_no": [],
                "license_type": [],
                "status": [],
                "orig_issue_date": [],
                "expiry": [],
                "renewed": []}

data_df = pd.DataFrame(data_dict)

# Get data on first page of search results
add_df = get_one_page_data(driver)
data_df = pd.concat([data_df,add_df],axis=0)
generate_csv(data_df)

# Get data on next pages of search results


# Quit driver
driver.quit()