import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.cv.lv/lv"

def scrape_cv_lv(driver, keywords, location, salary):
    jobs = []

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

        if location:
            location_input = driver.find_element(By.CSS_SELECTOR, ".search-form__locations .react-select__input-container > input")

            if len(location.split()) > 1:
                location_query = location.split(" ")
                for location in location_query:
                    location_input.send_keys(location)

                    time.sleep(1)
                    location_dropdown = driver.find_element(By.CSS_SELECTOR, ".react-select__menu-portal")
                    options = location_dropdown.find_elements(By.CSS_SELECTOR, ".react-select__option")
                    if options:
                        options[0].click()
            else:
                location_input.send_keys(location)
                time.sleep(1)

                location_dropdown = driver.find_element(By.CSS_SELECTOR, ".react-select__menu-portal")
                options = location_dropdown.find_elements(By.CSS_SELECTOR, ".react-select__option")
                if options:
                    options[0].click()

        if salary:
            toggle_more = driver.find_element(By.CSS_SELECTOR, ".search-form__additional-toggle button")
            toggle_more.click()

            time.sleep(2)
            salary_input = driver.find_element(By.CSS_SELECTOR, ".search-form__salary input.input-text__field")
            salary_input.send_keys(int(salary))
            salary_input.send_keys(Keys.RETURN)

        # Add delay for button update
        time.sleep(2)
        show_results_button = driver.find_element(By.CSS_SELECTOR, ".search-form-footer button")
        if "btn--type-disabled" in show_results_button.get_attribute('class').split():
            print("Try other filters")
            return
        show_results_button.click()

        print("Processing vacancies")
        time.sleep(5)
        job_cards = driver.find_elements(By.CLASS_NAME, "vacancies-list__item")

        for idx, card in enumerate(job_cards, start=1):
            # retrieve card info
            title = card.find_element(By.CLASS_NAME, "vacancy-item__title")
            location = card.find_element(By.CLASS_NAME, "vacancy-item__locations")

            jobs.append({
                "title": title.text,
                "location": location.text,
                "link": title.get_attribute('href')
            })

        print("Collected items successfully!")
        return jobs

    except Exception as e:
        print(f"An error occured: {e}")
        return []
