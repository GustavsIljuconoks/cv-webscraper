from utils.browser import get_driver
from scrapers.cv_lv import scrape_cv_lv

if __name__ == "__main__":
    print("Welcome to the job scraper!")

    keywords = input("Enter keywords: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")

    driver = get_driver()
    try:
        scrape_cv_lv(driver, keywords, location, salary)
    finally:
        driver.quit()
