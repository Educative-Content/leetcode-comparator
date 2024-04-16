from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import csv
import json

# Initialize ChromeDriver
def initiate_driver():
    try:
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument('--blink-settings=imagesEnabled=false')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    except Exception as error:
        print("There was some error in starting up the driver")
        print("Please try it again", str(error))

# Close ChromeDriver
def close_driver():
    driver.close()
    driver.quit()

def leetcode_saver(topics):
    # Open file in append mode
    with open('leetcode_data.csv', mode='w', newline='') as file:  
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['LeetcodeTopic'])
        for text in topics:
            writer.writerow([text])

def educative_saver(lessons):
    # Open file in append mode
    with open('educative_data.csv', mode='w', newline='') as file:  
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['EducativeLessons'])
        for text in lessons:
            writer.writerow([text])

def leetcode_scrapper(url, pages):
    driver.get(url)
    page_number = 1 
    topic_texts = []

    while True:
        try:
            sleep(2)
            # Waiting for all the topic to render
            topic = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='truncate']/a")))

        except StaleElementReferenceException as e:
            print("Page content was not properly rendered, Exiting the program!")
            print("Error", e)
            break

        for i in range(len(topic) - 1):
            text = topic[i].text

            # filtering extracted data
            space_index = text.find(' ')
            if space_index != -1:
                # Return the substring starting from the space
                topic_texts.append(text[space_index+1:])
            else:
                topic_texts.append(text)
                
        # Check if there is a next page
        next_button = driver.find_element(By.XPATH, '//button[@aria-label="next"]')
        
        # Exit loop if no next button or reached the last page
        if page_number == pages or not next_button:
            break
        
        sleep(5)
        next_button.click()
        # Increment page number
        page_number += 1

    # writing the scrapped data
    leetcode_saver(topic_texts)

def educative_scrapper(url):
    driver.get(url)
    lessons = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//a/span[contains(@class, 'text-base')]")))
    lesson_texts = []
    for i in range(len(lessons) - 1):
        text = lessons[i].text
        lesson_texts.append(text)
    educative_saver(lesson_texts)

def fetch_from_leetcode(url, pages):
    initiate_driver()
    leetcode_scrapper(url, pages)
    close_driver()

def fetch_from_educative(url):
    initiate_driver()
    educative_scrapper(url)
    close_driver()


# # Fetch data from LeetCode

# leetcode_url = "<LeetCodeURL>"
# fetch_from_leetcode(leetcode_url, pages=10)

# # Fetch data from Educative

# educative_url = "<EducativeURL>"
# fetch_from_educative(educative_url)
