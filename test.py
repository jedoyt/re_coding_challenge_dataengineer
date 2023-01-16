from module import *
from webdriver_manager.chrome import ChromeDriverManager
import time

# I. INPUT PREFERENCES

# Field Inputs
print("Input data on required fields to proceed.")
print("List of Professional Licenses:")
print(  "All, Certified Pharmacy Technician, Intern - Graduate, Intern - Student,\n",
        "Non-Resident Pharmacist, Non-Resident PIC, Pharmacist, Pharmacy Technician,\n",
        "Pharmacy Technician in Training, Practitioner Controlled Substance,\n",
        "Researcher Controlled Substance, Student Pharmacy Technician")

list_of_professionals = ['All', 'Certified Pharmacy Technician', 'Intern - Graduate', 'Intern - Student',
'Non-Resident Pharmacist', 'Non-Resident PIC', 'Pharmacist', 'Pharmacy Technician', 'Pharmacy Technician in Training',
'Practitioner Controlled Substance', 'Researcher Controlled Substance', 'Student Pharmacy Technician'
]

licensetype_select = str(input("Enter profession (Choose only from the list above): "))
while licensetype_select not in list_of_professionals:
    print("Profession not found. Please select only from the list above.")
    licensetype_select = str(input("Enter profession (Choose only from the list above): "))

lastname_str = str(input("Enter keyword for Last Name field: "))
# Other License options: 'All', 'Certified Pharmacy Technician', 'Intern - Graduate', 'Intern - Student',
# 'Non-Resident Pharmacist', 'Non-Resident PIC', 'Pharmacist', 'Pharmacy Technician', 'Pharmacy Technician in Training', 
# 'Practitioner Controlled Substance', 'Researcher Controlled Substance', 'Student Pharmacy Technician'

# II. SETUP WEBDRIVER
#driver_path = set_chromedriver_os(machine_os) # Setup driver path, select the machine's os

# Create instance of webdriver using Chrome browser
#service = Service(executable_path = driver_path)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://idbop.mylicense.com/verification/Search.aspx") # Get URL

# II. WEB AUTOMATION AND SCRAPING
# Enter field inputs and click search
input_and_search(driver, licensetype_select, lastname_str)

results_table_elem = driver.find_element(By.ID, "datagrid_results")
a_tags = results_table_elem.find_elements(By.TAG_NAME, "a") # All anchor tags from the table

# Separate names of the professionals from page nums of search results
pros_indices = [a_tags.index(tag) for tag in a_tags[1:] if tag.text.isnumeric() == False]
pagination_indices = [a_tags.index(tag) for tag in a_tags if tag.text.isnumeric()]

page_link_elems = [tag for tag in a_tags if tag.text.isnumeric()]

#print("No. of '<a>' tags:",len(a_tags))
#print("No. of Professionals:", len(pros_indices))
#print("No. of page results:", len(pagination_indices))
#print("Professionals:",pros_indices)
#print("Pagination indices:",pagination_indices)
print("Page Result Links:", [elem.text for elem in page_link_elems])

# Create initial DataFrame
data_dict = {"firstname":[],
                "middlename": [],
                "lastname": [],
                "license_no": [],
                "license_type": [],
                "status": [],
                "orig_issue_date": [],
                "expiry": [],
                "renewed": []}

df = pd.DataFrame(data_dict)

# Get data on first page of search results
add_df = get_one_page_data(driver)
df = pd.concat([df,add_df],axis=0)

# Get data on next pages of search results
if len(page_link_elems) > 0:
    for i in pagination_indices:
        results_table_elem = driver.find_element(By.ID, "datagrid_results")
        a_tags = results_table_elem.find_elements(By.TAG_NAME, "a") # All anchor tags from the table
        time.sleep(5)
        
        next_page = a_tags[i]
        print("Accessed element:",str(next_page))
        print("Now trying to click...")
        next_page.click()
        print("Accessed next page results!")

        add_df = get_one_page_data(driver)
        df = pd.concat([df,add_df],axis=0)
        print("Concatenated additional records!")

# IV. GENERATE REPORT IN csv FILE FORMAT
generate_csv(df=df,prof=licensetype_select,keyword=lastname_str)

# Quit driver
driver.quit()