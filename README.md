# Leetcode Comparator
This project is used to fetch data from LeetCode and Educative via Selenium and perform different comparisons with that data. The script fetches the following data to be exact:

- List of problems from the LeetCode Problems page
- List of lessons from any Educative published course

## How to run the script

Please follow the guidelines below to use the scripts.

### Prerequisites

- Python version > 3.9
- Selenium version ≥ 4.11.2
- chromedriver version compatible with chrome browser

#### Setup

- Please go through [this](https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test) tutorial to setup Python with Selenium.
- Make sure chromedriver is installed (it's usually installed at the time of chrome browser installation). If the chromedriver is not installed, we can get it from [here](https://sites.google.com/chromium.org/driver/).

### Script

The `scrapper.py` script is used to fetch data from LeetCode or Educative.

- From LeetCode, we fetch problem names displayed at the provided URL.
- From Educative, we fetch lesson names contained in the course hosted at the provided URL.

#### LeetCode

To fetch data from LeetCode, uncomment two lines below the comment `# Fetch data from LeetCode` and update the following values:
- Provide the LeetCode URL in the `leetcode_url` variable.
    -  This is the URL of the **Problems** page (https://leetcode.com/problemset/) that displays a list of problems. This list can be managed/sorted w.r.t. different criteria e.g., Tags, Difficulty, Frequency, etc.
- Provide number of pages to scrape in the `pages` parameter.

#### Educative

To fetch data from Educative, uncomment two lines below the comment `# Fetch data from Educative` and update the following values:
- Provide the Educative published course URL in the `educative_url` variable.

#### Output

When the script runs, the data is fetched and saved into the corresponding `.csv` file, i.e., `leetcode_data.csv` or `educative_data.csv`.

## How to compare the data

After we have the data, we need to compare it. In the LeetCode data, we need to find all those problems that aren't available in the Educative data. To do this:
1. Create a new Google Spreadsheet.
2. Import both sheets (`leetcode_data.csv` and `educative_data.csv`) as follows:
    - File > Import > Upload > Insert new sheet(s) > Import data 
3. Add the following formula in a new column in the LeetCode sheet: `=IFERROR(IF(MATCH(A1, educative_data!A:A,0),"Yes"),"No")`
