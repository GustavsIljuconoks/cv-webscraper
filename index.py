import time
import csv

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path


url = "https://www.cv.lv/lv"

def search_jobs(keywords, location, salary):
    service = Service(executable_path=binary_path)

    # add driver options for performance
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=service, options=option)

    try:
        driver.get(url)
        time.sleep(2)

        if keywords:
            # locate keyword input field
            search_input = driver.find_element(By.CSS_SELECTOR, ".search-form__keywords .react-select__input-container > input")

            if len(keywords.split()) > 1:
                search_query = keywords.split(" ")
                for search in search_query:
                    search_input.send_keys(search)
                    search_input.send_keys(Keys.RETURN)
            else:
                search_input.send_keys(keywords)
                search_input.send_keys(Keys.RETURN)

        if salary:
            toggle_more = driver.find_element(By.CSS_SELECTOR, ".search-form__additional-toggle button")
            toggle_more.click()

            time.sleep(2)
            salary_input = driver.find_element(By.CSS_SELECTOR, ".search-form__salary input.input-text__field")
            salary_input.send_keys(int(salary))
            salary_input.send_keys(Keys.RETURN)

        # TODO: Process location input
        if location:
            pass

        show_results_button = driver.find_element(By.CSS_SELECTOR, ".search-form-footer button")
        show_results_button.click()

        time.sleep(5)
        job_cards = driver.find_elements(By.CLASS_NAME, "vacancies-list__item")
        jobs = []

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
    print("Welcome to cv scraper!")
    keywords = input("Enter keywords: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")

    search_jobs(keywords, location, salary)

