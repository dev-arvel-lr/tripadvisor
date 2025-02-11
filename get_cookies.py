from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time
import pickle
import undetected_chromedriver as uc


try:
    # Set up Chrome options
    chrome_options = Options()

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # proxy = "https://AbCdEf654321:AbCdEf123456_country-jp@geo.iproyal.com:12321"

    # Path to the proxy extension (if needed)
    proxy_extension_path = r"C:\Users\franc\OneDrive\Documents\TripAdvisor\proxy_extension" 
    chrome_options.add_argument("--load-extension=" + proxy_extension_path)

    # # Specify the path to chromedriver
    # service = Service("C:/Drivers/chromedriver.exe")

    # Initialize the WebDriver with options
    driver = uc.Chrome(options=chrome_options)

    # Open the website
    driver.get("https://www.google.com/")
    
    # Sleep for 1 minute (60 seconds)
    print("Waiting for 1 mins to login.")
    time.sleep(60)
    
    # Get cookies from the current session
    # cookies = driver.get_cookies()
    
    # # Print the cookies to see what you're getting
    # print(cookies)
    
    # # Save cookies to a file (optional)
    # with open("cookies1.pkl", "wb") as file:
    #     for cookie in cookies:
    #     file.write(f"{cookie['name']}={cookie['value']}\n")  

    # Keep the browser open for inspection
    input("Press Enter to close the browser...")

except WebDriverException as e:
    print(f"An error occurred: {e}")
    if driver:
        driver.quit()
