import pyautogui
import pyperclip
import time
import csv
import os
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
import subprocess
import undetected_chromedriver as uc

# Disable the PyAutoGUI fail-safe (Not Recommended)
pyautogui.FAILSAFE = False

def open_chrome_with_debugging():
    # Step 1: Open Chrome with remote debugging enabled
    pyautogui.moveTo(947, 1056, duration=1.5, tween=pyautogui.easeInOutQuad)  # Example coordinates for taskbar, change as needed
    pyautogui.click()

    # Wait for Chrome to open
    time.sleep(5)


def attach_selenium_to_chrome():
    # Define proxy settings
    # proxy = "http://AbCdEf654321:AbCdEf123456_country-jp@geo.iproyal.com:12321"  # Replace with your IPRoyal proxy details
    
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options = {
    'proxy': {
        'http': 'http://AbCdEf654321:AbCdEf123456_country-jp@geo.iproyal.com:12321', 
        'https': 'http://AbCdEf654321:AbCdEf123456_country-jp@geo.iproyal.com:12321',
        'no_proxy': 'localhost,127.0.0.1' # excludes
        }
    }
    # Add proxy to Chrome options
    # chrome_options.add_argument(f"--proxy-server={proxy}")
    
    # Start a new Selenium driver attached to the existing Chrome instance
    driver = uc.Chrome(options=chrome_options, seleniumwire_options=options)
    return driver

def main():
    # Start Chrome with remote debugging enabled
    subprocess.Popen(r'"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" --remote-debugging-port=9222 --user-data-dir="C:\Chrome_debug"')
    pyautogui.moveTo(947, 1056, duration=1.5, tween=pyautogui.easeInOutQuad)  # Example coordinates for taskbar, change as needed
    pyautogui.click()
    open_chrome_with_debugging()
    driver = attach_selenium_to_chrome()
    driver.get("https://iproyal.com/ip-lookup/")  # Check if the proxy is working
    # driver.get("https://www.tripadvisor.com/CreateListing.html")
    
    input("Press Enter to close the browser...")
    # time.sleep(20)

if __name__ == "__main__":
    main()
