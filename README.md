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
1. Make sure you have Python 3 and Chrome browser installed
2. Your version of Chrome must match with the existing chromedriver of this repo
  - installed version of webdrivers: 109.0.5414.74
  - link to source of webdrivers: https://chromedriver.storage.googleapis.com/index.html
3. Install all required packages. Go to command line and make sure that you are on this project directory. Do the following instructions below before moving to step 4:
  - It is recommended also to create a virtual environment first to avoid messing up with the versions of your current packages in Python
    - `$ python3 -m venv venv` (Creates a virtual environment within the project directory)
    - `$ source venv/bin/activate` (Activates the virtual environment. After activating, you may now install the packages.
  - `$ pip install -r requirements.txt` (Installs the required packages)
4. Run `main.py`
  - Once it runs, the command line will ask for the following inputs:
    - `Select OS (linux, mac, or win): ` (choices are limited to these three--- linux, mac, win. No need to enclose in quotes.)
      - Once entered, the command line with display the machine's current version of Chrome and the existing version of Chrome Driver. Any significant discrepancy on versions may affect the performance of the program.
      - The link to the source of Chrome's webdrivers are also provided if there is a need to update or downgrade the webdriver to match your current Chrome browser version
    - `Enter profession: ` (Choose the profession as shown on list. Case sensitive, and also NO NEED to enclose in quotes.)
    - `Enter keyword for Last Name field: ` (Enter search string keyword for the last name. Again, NO NEED to enclose in quotes.)
5. Once you see the prompt, `Generated report file: 'records_xxxxxxxxxx_(xxxxx+xxxxx>).csv'!`, go to the project folder to see the report as a csv file having this filename format; `records_<timestamp>_(<profession+keyword>).csv`.
