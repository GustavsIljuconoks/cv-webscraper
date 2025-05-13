from utils.browser import get_driver
from utils.search_history import add_search_to_history, load_search_history
from scrapers.cv_lv import scrape_cv_lv
from scrapers.visidarbi_lv import scrape_visidarbi_lv
import csv

if __name__ == "__main__":
    print("Welcome to the job scraper!")
    print("1. Start search ")
    print("2. Check searched history")

    choice = input("Enter number (1, 2): ")

    if int(choice) == 1:
        keywords = input("Enter keywords: ")
        location = input("Enter location: ")
        salary = input("Enter salary: ")

        driver = get_driver()
        jobs = []

        try:
            print("\nScraping jobs from visidarbi.lv...")
            jobs.extend(scrape_visidarbi_lv(driver, keywords, location, salary))

            print("\nScraping jobs from cv.lv...")
            jobs.extend(scrape_cv_lv(driver, keywords, location, salary))

            if jobs:
                with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=["title", "location", "link"])
                    writer.writeheader()
                    for job in jobs:
                        writer.writerow(job)

                add_search_to_history(keywords, location, salary, len(jobs))
            else:
                print("No jobs were collected.")

        finally:
            driver.quit()
    if int(choice) == 2:
        history = load_search_history()

        if not history:
            print("No search history found.")
        else:
            print("\nRecent Searches:")
            print("-" * 50)
            for i, entry in enumerate(history, 1):
                print(f"{i}. Keywords: {entry['keywords']} | Location: {entry['location']} | Salary: {entry['salary']} | Found results: {entry['results']} | Date: {entry['timestamp']}")
            print("-" * 50)

