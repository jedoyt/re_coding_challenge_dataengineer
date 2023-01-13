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

## Preparations before running main.py
1. Make use have Chrome browser installed
2. Install all required packages. Go to command line and make sure that you are on the project directory. Run the code below:
  `$ pip install -r requirements.txt`
3. On line 14 of main.py, Choose the right OS for the chromedriver by changing the second argument next to `os.getcwd()`
  choices: `linux`, `mac`, `win`
5. Run `main.py`
