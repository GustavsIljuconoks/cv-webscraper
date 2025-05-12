import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

url = "https://www.visidarbi.lv/"

def scrape_visidarbi_lv(driver, keywords, location, salary):
    jobs = []
    page_number = 1 

    try:
        driver.get(url)
        time.sleep(2)

        if keywords:
            search_input = driver.find_element(By.CSS_SELECTOR, ".twitter-typeahead input.tt-input")
            search_input.send_keys(keywords)
            search_input.send_keys(Keys.RETURN)

        if location:
            location_input = driver.find_element(By.CSS_SELECTOR, "#job-location-search-selectized")
            location_input.send_keys(location)
            time.sleep(1)
            try:
                location_dropdown = driver.find_element(By.CSS_SELECTOR, ".selectize-dropdown")
                options = location_dropdown.find_elements(By.CSS_SELECTOR, ".selectize-dropdown .option")
                if options:
                    options[0].click()
            except NoSuchElementException:
                pass

        if salary:
            try:
                toggle_more = driver.find_element(By.CSS_SELECTOR, "a.vd-btn-1.small.more")
                toggle_more.click()
                time.sleep(2)
                salary_input = driver.find_element(By.CSS_SELECTOR, "#filter-salary-from")
                salary_input.clear()  
                salary_input.send_keys(str(salary))
                salary_input.send_keys(Keys.RETURN)
            except NoSuchElementException:
                pass

        # Add delay for button update
        time.sleep(2)
        try:
            show_results_button = driver.find_element(By.CSS_SELECTOR, "a#search-btn")
            if "btn--type-disabled" in show_results_button.get_attribute('class').split():
                return
            show_results_button.click()
        except NoSuchElementException:
            pass

        wait = WebDriverWait(driver, 5)

        # pagination loop
        while True:
            try:
                job_cards = wait.until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".list.inner.search-page .item")))

                for card in job_cards:
                    try:
                        title_element = card.find_element(By.CSS_SELECTOR, "div.title h3 a")
                        title = title_element.text
                        link = title_element.get_attribute("href")
                    except NoSuchElementException:
                        continue 

                    try:
                        location = card.find_element(By.CSS_SELECTOR, "li.location span").text
                    except NoSuchElementException:
                        location = "Location not specified"

                    jobs.append({
                        "title": title,
                        "location": location,
                        "link": link or "#"
                    })

            except TimeoutException:
                break  

            # Try to find the next page number link
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, f"ul.pagination li:nth-child({page_number + 1}) a")
                next_page.click()
                time.sleep(3) 
                page_number += 1
            except NoSuchElementException:
                break  
        return jobs
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
