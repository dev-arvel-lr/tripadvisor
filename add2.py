from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time
import pickle
import undetected_chromedriver as uc
import os
try:
    # Set up Chrome options
    chrome_options = Options()

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # proxy = "https://AbCdEf654321:AbCdEf123456_country-jp@geo.iproyal.com:12321"

    # # Path to the proxy extension (if needed)
    # proxy_extension_path = r"C:\Users\franc\OneDrive\Documents\TripAdvisor\proxy_extension" 
    # chrome_options.add_argument("--load-extension=" + proxy_extension_path)

    # # Specify the path to chromedriver
    # service = Service("C:/Drivers/chromedriver.exe")

    # Initialize the WebDriver with options
    driver = uc.Chrome(options=chrome_options)

    # Open the website
    driver.get("https://www.tripadvisor.com/CreateListing.html")
    
    cookies_file = "cookies1.pkl"
    
    try:
        if not os.path.exists(cookies_file) or os.stat(cookies_file).st_size == 0:
            raise FileNotFoundError("Error: No cookies found. Please log in and save cookies first.")

        with open(cookies_file, "rb") as file:
            cookies = pickle.load(file)
            if not cookies:
                raise ValueError("Error: The cookies file is empty.")
            
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.refresh()

    except (FileNotFoundError, pickle.UnpicklingError, EOFError, ValueError) as e:
        print(f"Error: {e}")
    
    
    
    # Sleep for 1 minute (60 seconds)
    # time.sleep(60)
    
    # # Get cookies from the current session
    # cookies = driver.get_cookies()
    
    # # Print the cookies to see what you're getting
    # print(cookies)
    
    # # Save cookies to a file (optional)
    # with open("cookies.pkl", "wb") as file:
    #     pickle.dump(cookies, file)

    # Keep the browser open for inspection
    input("Press Enter to close the browser...")

except WebDriverException as e:
    print(f"An error occurred: {e}")
    if driver:
        driver.quit()
