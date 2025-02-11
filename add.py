import random
import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time
import pickle
import undetected_chromedriver as uc
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv



load_dotenv()

def type_delay(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(2, 4))

PROXY_EXTENSION_PATH =  os.getenv("PROXY_EXTENSION_PATH")

try:
    name = "Stephen Hotel"
    chrome_options = Options()
    
        
    # Set up Chrome options
    ua = UserAgent()
    user_agent = ua.random
    chrome_options.add_argument(f"user-agent={user_agent}") 

    
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")


    # # Path to the proxy extension (if needed)
    proxy_extension_path = PROXY_EXTENSION_PATH
    chrome_options.add_argument("--load-extension=" + proxy_extension_path)

    # # Specify the path to chromedriver
    # service = Service("C:/Drivers/chromedriver.exe")

    # Initialize the WebDriver with options
    driver = uc.Chrome(options=chrome_options)

    # Open the website
    driver.get("https://www.google.com/")

    # wait = WebDriverWait(driver, 20)
    # cookies_file = "cookies1.pkl"
    
    # try:
    #     if not os.path.exists(cookies_file) or os.stat(cookies_file).st_size == 0:
    #         raise FileNotFoundError("Error: No cookies found. Please log in and save cookies first.")

    #     with open(cookies_file, "rb") as file:
    #         cookies = pickle.load(file)
    #         if not cookies:
    #             raise ValueError("Error: The cookies file is empty.")
            
    #         for cookie in cookies:
    #             driver.add_cookie(cookie)

    #     driver.refresh()

    # except (FileNotFoundError, pickle.UnpicklingError, EOFError, ValueError) as e:
    #     print(f"Error: {e}")
        
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(random.uniform(2, 4))
        
    # text_input_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, r'#\:lithium-R49ceuinjlq\:')))

    # type_delay(text_input_name, name)
   
    

    
   

    # driver.get("https://www.google.com/")
    
    
    # text_search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, r'#APjFqb')))
    
    # type_delay(text_search, "https://www.tripadvisor.com/CreateListing.html")
    
    # wait.until(EC.element_to_be_clickable(text_search))
    # text_search.send_keys(Keys.RETURN)
    
    
    # first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3')))
    
    # actions = ActionChains(driver)
    # actions.move_to_element(first_result).click().perform()
    
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    
   
    
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
