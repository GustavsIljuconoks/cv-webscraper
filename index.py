import argparse
import time
import csv

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path


url = "https://www.cv.lv/lv"

def search_jobs(keywords):
    service = Service(executable_path=binary_path)

    # add driver options for performance
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless=new")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=service, options=option)

    try:
        driver.get(url)
        time.sleep(2)

        # locate keyword input field
        search_input = driver.find_element(By.CSS_SELECTOR, ".search-form__keywords .react-select__input-container > input")

        search_query = ' '.join(keywords)
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)

        show_results_button = driver.find_element(By.CSS_SELECTOR, ".search-form-footer button")
        show_results_button.click()

        time.sleep(5)

        job_cards = driver.find_elements(By.CLASS_NAME, "vacancies-list__item")
        jobs = []

        print(f"Search results for '{keywords}':\n")
        for idx, card in enumerate(job_cards, start=1):
            # retrieve card info
            title = card.find_element(By.CLASS_NAME, "vacancy-item__title")
            location = card.find_element(By.CLASS_NAME, "vacancy-item__locations")

            jobs.append({
                "title": title.text,
                "location": location.text,
                "link": title.get_attribute('href'),
            })

        print("Collected items successfully!")
        with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "location", "link"])
            writer.writeheader()
            writer.writerows(jobs)

    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for jobs on cv.lv")
    parser.add_argument("keywords", nargs="+", help="Keywords to search for")
    args = parser.parse_args()

    search_jobs(args.keywords)

