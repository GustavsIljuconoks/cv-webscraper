from utils.browser import get_driver
from scrapers.cv_lv import scrape_cv_lv
from scrapers.visidarbi_lv import scrape_visidarbi_lv
import csv

if __name__ == "__main__":
    print("Welcome to the job scraper!")

    keywords = input("Enter keywords: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")

    driver = get_driver()
    jobs = []  
    
    try:
        jobs.extend(scrape_visidarbi_lv(driver, keywords, location, salary))
        jobs.extend(scrape_cv_lv(driver, keywords, location, salary))
        
        if jobs:
            with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["title", "location", "link"])
                writer.writeheader()
                for job in jobs:
                    writer.writerow(job)
        else:
            print("No jobs were collected.")
            
    finally:
        driver.quit()
