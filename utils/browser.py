from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

def get_driver():
    service = Service(executable_path=binary_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    return webdriver.Chrome(service=service, options=options)

