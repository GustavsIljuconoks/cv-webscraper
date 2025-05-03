import argparse
import time

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

        # TODO: get correct selector for keyword input
        # locate keyword input field
        search_input = driver.find_element(By.CSS_SELECTOR, ".search-form__keywords .react-select__input")
        print(search_input)

        search_input.clear()
        search_input.send_keys(keywords)
        search_input.send_keys(Keys.RETURN)


        show_results_button = driver.find_element(By.CSS_SELECTOR, "button.jsx-2929518284")
        show_results_button.click()

        time.sleep(5)

        # retrieve job job titles
        job_titles = driver.find_elements(By.CSS_SELECTOR, "div[class*='vacancy-item__title']")

        print(f"Search results for '{keywords}':\n")
        for idx, title in enumerate(job_titles, start=1):
            print(f"{idx}. {title.text}")


    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for jobs on cv.lv")
    parser.add_argument("keywords", help="Keywords to search for")
    args = parser.parse_args()

    search_jobs(args.keywords)

