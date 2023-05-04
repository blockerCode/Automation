import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_you_tube(channel):
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.youtube.com/')
        input_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="search"]'))
        )
        input_box.send_keys(channel)
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="search-icon-legacy"]'))
        )
        search_box.click()
        time.sleep(10)
    except Exception as e:
        print(f"Error is :::: {str(e)}")


if __name__ == "__main__":
    channel_name = sys.argv[1:]
    open_you_tube(channel_name)


