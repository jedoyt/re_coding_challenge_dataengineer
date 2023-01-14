from module import *

# I. INPUT PREFERENCES
# Set machine's os: 'linux', 'mac', 'win'
machine_os = 'mac'

# Field Inputs
licensetype_select = "Pharmacist"
lastname_str = "L"

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

# Scrape data from page
get_one_page_data(driver)

# V. GENERATE REPORT
# Generate csv report
generate_df_and_csv()

driver.quit()