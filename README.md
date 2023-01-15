# re_coding_challenge_dataengineer
A coding challenge that uses the web scraping automation of Selenium and Dataframing of Pandas library. The output is the `records.csv` file containing the scraped data.

# Coding Challenge for Data Engineer
This coding problem is a small picture of the kind of work the scraping team does and is an opportunity for you to demonstrate your skills.

Write a script to scrape data from the Idaho License Verification website: idbop.mylicense.com/verification/Search.aspx.

Please do this in Python 3 and share the code as a GitHub link.
The script should return all Pharmacists with a last name that starts with "L" as a .csv file with the following information:
- First Name
- Middle Name
- Last Name
- License Number
- License Type
- Status
- Original Issued Date
- Expiry
- Renewed

The script should be written to be able to easily adapt to returning a different license type and different last name starting letter.

## Quick Steps
1. Make use have Chrome browser installed
2. Your version of Chrome must match with the existing chromedriver of this repo
  - installed version of drivers: 109.0.5414.74
  - link to source of drivers: https://chromedriver.storage.googleapis.com/index.html
3. Install all required packages. Go to command line and make sure that you are on the project directory. Run the code below:
  - It is recommended also to create a virtual environment first to avoid messing up with the versions of your current packages in Python
    - `$ python3 -m venv venv` (Creates a virtual environment within the project directory)
    - `$ source venv/bin/activate` (Activates the virtual environment. After activating, you may now do the `pip install`'s
  - `$ pip install -r requirements.txt` (Installs the required packages)
4. Run `main.py`
  - Once it runs, the command line with ask for the following inputs:
    - `Select OS (linux, mac, or win): ` (choices are limited to these three--- linux, mac, win. No need to enclose in quotes.)
      - Once entered, the command line with display the machine's current version of Chrome and the existing version of Chrome Driver
      - The link to the source of Chrome's webdrivers are also provided if there is a need to update or downgrade the webdriver to match your current Chrome browser version
    - `Enter profession: ` (Choose the profession as shown on list. Case sensitive, and also no need to enclose in quotes.)
    - `Enter keyword for Last Name field: ` (Enter search string keyword for the last name. Again, no need to enclose in quotes.)
5. Check the report from the generated `records_<timestamp>_(<search+strings>).csv` file
