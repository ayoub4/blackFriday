import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

url = "https://nextlevelpc.ma/promo-try/"

def fetch_data():
    url = "https://nextlevelpc.ma/promo-try/"  # Replace this with your actual URL
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad requests
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find(class_="elementor-alert-title")

    return elements

def monitor_changes():
    i = 0
    while True:
        current_data = fetch_data()
        if "L'offre est expirée" not in current_data:
            options = Options()
            options.headless = True  # Set to False if you want to see the Firefox window
            driver = webdriver.Firefox(options=options)
            driver.get(url)

            break
        print("attempt " + str(i) + " failed")
        i += 1
        time.sleep(10)

if __name__ == "__main__":
    monitor_changes()
