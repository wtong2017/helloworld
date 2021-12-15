"""Main module."""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from selenium.webdriver.chrome.options import Options

import pandas as pd
import time
from bs4 import BeautifulSoup

targets = pd.read_csv("./helloworld/data.csv")


chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-extensions')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_experimental_option('w3c', True)

#This example requires Selenium WebDriver 3.13 or newer

with webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options) as driver:
    for name, item in targets.iterrows():
        print(item)
        time.sleep(3)
        driver.get(item.link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup.prettify())
        wait = WebDriverWait(driver, 10)
        # driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
        first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "video source")))
        print(first_result.get_attribute("src"))
        break