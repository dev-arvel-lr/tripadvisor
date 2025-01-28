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
import subprocess


# Disable the PyAutoGUI fail-safe (Not Recommended)
pyautogui.FAILSAFE = False

# Click probabilities
# click_probabilities = {
#     1: 0.398,
#     2: 0.187,
#     3: 0.102,
#     4: 0.074,
#     5: 0.051,
#     6: 0.045,
#     7: 0.034,
#     8: 0.026,
#     9: 0.024,
#     10: 0.022,
#     'none': 0.037
# }

# def read_params_from_file(filename):
#     params = {}
#     with open(filename, 'r', encoding='utf-8-sig') as file:
#         for line in file:
#             key, value = line.strip().split(':', 1)
#             params[key.strip()] = value.strip()
#     return params

# def read_execution_ratios_from_csv(filename):
#     execution_ratios = {}
#     with open(filename, mode='r', encoding='utf-8-sig') as csvfile:
#         # Manually skip the first line
#         for _ in range(1):
#             next(csvfile)

#         # Now use DictReader to parse the file starting from the headers
#         csv_reader = csv.DictReader(csvfile)

#         # Print the headers detected by the CSV reader
#         print("CSV Headers Detected:", csv_reader.fieldnames)

#         # Iterate over the rows
#         for row in csv_reader:
#             time_str = row['Time'].strip()
#             # Skip if time_str is empty
#             if not time_str:
#                 continue

#             # Convert time to format 'HH:MM' and handle errors
#             time_parts = time_str.split(':')
#             if len(time_parts) == 2:
#                 try:
#                     hour = int(time_parts[0].strip())
#                     minute = int(time_parts[1].strip())
#                     time = f"{hour:02}:{minute:02}"
#                 except ValueError:
#                     print(f"Skipping invalid time value: {time_str}")
#                     continue
#             else:
#                 print(f"Skipping malformed time entry: {time_str}")
#                 continue

#             try:
#                 ratio = float(row['Execution Ratio'].strip().replace('%', '')) / 100
#                 execution_ratios[time] = ratio
#             except ValueError:
#                 print(f"Skipping invalid execution ratio value for time {time}")
#                 continue
#     print("CSV Headers Detected:", execution_ratios)
    
#     return execution_ratios

def calculate_sleep_interval(current_time, searches_per_day, execution_ratios):
    hour = current_time.strftime("%H:00")
    execution_ratio = execution_ratios.get(hour, 0.0)
    hourly_searches = searches_per_day * execution_ratio
    if hourly_searches == 0:
        return 3600
    base_interval = 3600 / hourly_searches
    variation = random.uniform(0.8, 1.2)
    sleep_interval = base_interval * variation
    return sleep_interval

def should_click_link(index):
    """Determine if a link should be clicked based on its index."""
    probability = click_probabilities.get(index, click_probabilities['none'])
    return random.random() < probability

def open_chrome_with_debugging():
    # Step 1: Open Chrome with remote debugging enabled
    pyautogui.moveTo(947, 1056, duration=1.5, tween=pyautogui.easeInOutQuad)  # Example coordinates for taskbar, change as needed
    pyautogui.click()

    # Wait for Chrome to open
    time.sleep(5)

def attach_selenium_to_chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    
    # Start a new Selenium driver attached to the existing Chrome instance
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# def slow_scroll_down(driver, pixels=100, delay=0.2):
#     """Scroll down the page slowly."""
#     scroll_height = driver.execute_script("return document.body.scrollHeight;")
#     for _ in range(0, scroll_height, pixels):
#         driver.execute_script(f"window.scrollBy(0, {pixels});")
#         time.sleep(delay)

# def slow_scroll_up(driver, pixels=100, delay=0.2):
#     """Scroll up the page slowly."""
#     scroll_height = driver.execute_script("return document.body.scrollHeight;")
#     for _ in range(0, scroll_height, pixels):
#         driver.execute_script(f"window.scrollBy(0, -{pixels});")
#         time.sleep(delay)


# def search_google(keyword, driver):
#     # Step 1: Go to the Google homepage
#     driver.get('https://www.google.com')

#     try:
#         # Step 2: Wait for the search input field to be present
#         search_box = WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located((By.NAME, 'q'))
#         )
#     except TimeoutException:
#         print("Timeout while waiting for search box, checking page source...")
#         print(driver.page_source)
#         return []

#     # Step 3: Clear the search box and type the query character by character
#     search_box.clear()
#     for char in keyword:
#         search_box.send_keys(char)
#         time.sleep(random.uniform(0.1, 0.3))  # Simulate human typing speed

#     # Step 4: Submit the search query by pressing the "Enter" key
#     search_box.send_keys(u'\ue007')  # Unicode for Enter key

#     # Step 5: Wait for the search results to load
#     WebDriverWait(driver, 15).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.tF2Cxc'))
#     )

#     # Step 6: Scroll slowly through the search results page
#     slow_scroll_down(driver, pixels=100, delay=0.3)
#     time.sleep(2)
#     slow_scroll_up(driver, pixels=100, delay=0.2)

#     # Step 7: Extract search results using Selenium
#     results = []
#     items = driver.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')
#     for item in items:
#         try:
#             # Check if the result is sponsored by checking for specific elements
#             sponsored_element = item.find_elements(By.CSS_SELECTOR, 'span.U3A9Ac.qV8iec')
#             is_sponsored = bool(sponsored_element) and "スポンサー" in item.text

#             # Extract the title and link
#             title_element = item.find_element(By.CSS_SELECTOR, 'h3')
#             link_element = item.find_element(By.CSS_SELECTOR, 'a')
            
#             if title_element and link_element:
#                 title_text = title_element.text
#                 link_href = link_element.get_attribute('href')
                
#                 results.append((title_text, link_href, is_sponsored))
#                 print(f"Google Search Result: {title_text} - {link_href} - {'Sponsored' if is_sponsored else 'Non-Sponsored'}")

#         except NoSuchElementException as e:
#             print(f"Error locating element: {e}")
#             continue

#     return results

def search_google(keyword, driver):
    # Step 1: Go to the Google homepage
    driver.get('https://www.google.com')

    try:
        # Step 2: Wait for the search input field to be present
        search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
    except TimeoutException:
        print("Timeout while waiting for search box, checking page source...")
        print(driver.page_source)
        return []

    # Step 3: Clear the search box and type the query character by character
    search_box.clear()
    for char in keyword:
        search_box.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Simulate human typing speed

    # Step 4: Submit the search query by pressing the "Enter" key
    search_box.send_keys(u'\ue007')  # Unicode for Enter key

    # Step 5: Wait for the search results to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.tF2Cxc'))
    )

    # Step 6: Scroll slowly through the search results page
    # slow_scroll_down(driver, pixels=100, delay=0.3)
    # time.sleep(2)
    # slow_scroll_up(driver, pixels=100, delay=0.2)

    # Step 7: Find and click the first result
    try:
        # first_result = driver.find_element(By.CSS_SELECTOR, 'div.tF2Cxc a')  # Find the first link directly
        # first_result.click()  # Click the first 
        driver.get("https://www.tripadvisor.jp/CreateListing.html")
        print("Clicked the first result.")
    except NoSuchElementException as e:
        print(f"Error locating the first result: {e}")
    except Exception as e:
        print(f"Error clicking the first result: {e}")
    
    return []
# def search_yahoo(keyword, driver):
#     # Step 1: Go to the Yahoo Japan homepage
#     driver.get('https://yahoo.co.jp')

#     try:
#         # Step 2: Wait for the search input field to be present
#         search_box = WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located((By.NAME, 'p'))  # 'p' is the name attribute for Yahoo's search box
#         )
#     except TimeoutException:
#         print("Timeout while waiting for search box, checking page source...")
#         print(driver.page_source)
#         return []

#     # Step 3: Clear the search box and type the query character by character
#     search_box.clear()
#     for char in keyword:
#         search_box.send_keys(char)
#         time.sleep(random.uniform(0.1, 0.3))  # Simulate human typing speed

#     # Step 4: Submit the search query by pressing the "Enter" key
#     search_box.send_keys(u'\ue007')  # Unicode for Enter key

#     # Step 5: Wait for the search results to load
#     WebDriverWait(driver, 15).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sw-CardBase'))
#     )

#     # Step 6: Scroll slowly through the search results page
#     slow_scroll_down(driver, pixels=100, delay=0.3)
#     time.sleep(2)
#     slow_scroll_up(driver, pixels=100, delay=0.2)

#     # Step 7: Extract search results using Selenium
#     results = []
#     items = driver.find_elements(By.CSS_SELECTOR, 'div.sw-CardBase')
#     for item in items:
#         # Check if the result is sponsored
#         is_sponsored = False
#         try:
#             sponsor_badge = item.find_element(By.CSS_SELECTOR, 'span.sw-Badge__text')
#             if sponsor_badge.text == "スポンサー":
#                 is_sponsored = True
#         except NoSuchElementException:
#             is_sponsored = False

#         try:
#             # Extract title
#             title_element = item.find_element(By.CSS_SELECTOR, 'h3')
#             title = title_element.text

#             # Extract link
#             link_element = item.find_element(By.CSS_SELECTOR, 'a')
#             link = link_element.get_attribute('href')

#             # Append result to the list
#             results.append((title, link, is_sponsored))
#             print(f"Yahoo Search Result: {title} - {link} - {'Sponsored' if is_sponsored else 'Non-Sponsored'}")
#         except NoSuchElementException as e:
#             print(f"Error locating element: {e}")
#             continue

#     return results

# def click_link(results, driver):
#     if results is None or len(results) == 0:
#         print("No results to click.")
#         return None

#     rand_num = random.random()
#     cumulative_probability = 0.0
#     for rank, probability in click_probabilities.items():
#         cumulative_probability += probability
#         if rand_num <= cumulative_probability:
#             if rank == 'none':
#                 print("No click this time.")
#                 return None
#             elif rank <= len(results):
#                 title, link, is_sponsored = results[rank - 1]
#                 if is_sponsored:
#                     print(f"Skipping sponsored link: {title} - {link}")
#                     continue
#                 print(f"Clicking on {rank} position: {title} - {link}")
#                 try:
#                     driver.get(link)

#                     # Scroll down to the bottom of the page slowly
#                     slow_scroll_down(driver, pixels=100, delay=0.3)
#                     time.sleep(2)  # Wait a bit after scrolling

#                     # Scroll back up to the top of the page slowly
#                     slow_scroll_up(driver, pixels=100, delay=0.1)
#                     time.sleep(5)  # Wait a bit after scrolling

#                     # Go back to the search results page
#                     driver.back()
#                     return link
#                 except Exception as e:
#                     print(f"Error clicking link {link}: {e}")
#                     return None
#             else:
#                 print("Rank exceeds the number of results.")
#                 return None
#     print("No click this time by default.")
#     return None

# def click_next_page(driver):
#     try:
#         next_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[@id='pnnext']"))
#         )
#         next_button.click()
#         time.sleep(4)
#         print('next')
        
#         # Step 5: Wait for the search results to load
#         WebDriverWait(driver, 15).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.tF2Cxc'))
#         )

#         # Step 6: Scroll slowly through the search results page
#         slow_scroll_down(driver, pixels=100, delay=0.3)
#         time.sleep(2)
#         slow_scroll_up(driver, pixels=100, delay=0.2)

#         # Step 7: Extract search results using Selenium
#         results = []
#         items = driver.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')
#         for item in items:
#             try:
#                 # Check if the result is sponsored by checking for specific elements
#                 sponsored_element = item.find_elements(By.CSS_SELECTOR, 'span.U3A9Ac.qV8iec')
#                 is_sponsored = bool(sponsored_element) and "スポンサー" in item.text

#                 # Extract the title and link
#                 title_element = item.find_element(By.CSS_SELECTOR, 'h3')
#                 link_element = item.find_element(By.CSS_SELECTOR, 'a')
                
#                 if title_element and link_element:
#                     title_text = title_element.text
#                     link_href = link_element.get_attribute('href')
                    
#                     results.append((title_text, link_href, is_sponsored))
#                     print(f"Google Search Result: {title_text} - {link_href} - {'Sponsored' if is_sponsored else 'Non-Sponsored'}")

#             except NoSuchElementException as e:
#                 print(f"Error locating element: {e}")
#                 continue
#         return results
#     except TimeoutException:
#         print("Next button not found, ending search.")

# def click_next_page_yahoo(driver):
#     try:
#         # Step 1: Wait for the "Next" button to be clickable and then click it
#         next_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='次のページ']"))
#         )
#         next_button.click()
#         time.sleep(4)  # Wait for the page to load
#         print('Navigated to next page on Yahoo')

#         # Step 2: Wait for the new search results to load
#         WebDriverWait(driver, 15).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sw-CardBase'))
#         )

#         # Step 3: Scroll slowly through the search results page
#         slow_scroll_down(driver, pixels=100, delay=0.3)
#         time.sleep(2)
#         slow_scroll_up(driver, pixels=100, delay=0.2)

#         # Step 4: Extract search results using Selenium
#         results = []
#         items = driver.find_elements(By.CSS_SELECTOR, 'div.sw-CardBase')
#         for item in items:
#             try:
#                 # Check if the result is sponsored
#                 is_sponsored = False
#                 try:
#                     sponsor_badge = item.find_element(By.CSS_SELECTOR, 'span.sw-Badge__text')
#                     if sponsor_badge.text == "スポンサー":
#                         is_sponsored = True
#                 except NoSuchElementException:
#                     is_sponsored = False

#                 # Extract title
#                 title_element = item.find_element(By.CSS_SELECTOR, 'h3')
#                 title = title_element.text

#                 # Extract link
#                 link_element = item.find_element(By.CSS_SELECTOR, 'a')
#                 link = link_element.get_attribute('href')

#                 # Append result to the list
#                 results.append((title, link, is_sponsored))
#                 print(f"Yahoo Search Result: {title} - {link} - {'Sponsored' if is_sponsored else 'Non-Sponsored'}")

#             except NoSuchElementException as e:
#                 print(f"Error locating element: {e}")
#                 continue
#         return results
#     except TimeoutException:
#         print("Next button not found or timed out, ending search.")
#         return []

# def save_searched_keyword(filename, search_site, keyword, ip_address, result):
#     search_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(f"{filename}.txt", "a", encoding='utf-8') as file:
#         file.write(f"{search_time} - {search_site} - {keyword} - {ip_address} - {result}\n")

def main():
    # # Read parameters from the text file
    # params = read_params_from_file('params1.txt')
    # keyword_text = params.get('keyword', '')
    # keyword_list = [item.strip() for item in keyword_text.split(",")]
    # searches_per_day = int(params.get('number of searches per day', 1))
    # industry = params.get('industry type', '')
    # keyword_len = len(keyword_list)


    # # Read execution ratios based on the industry type
    # if industry == 'food':
    #     csv_filename = os.path.join(os.path.dirname(__file__), 'food_industry_ratios.csv')
    #     execution_ratios = read_execution_ratios_from_csv(csv_filename)
    # elif industry == 'resignation':
    #     csv_filename = os.path.join(os.path.dirname(__file__), 'resignation_agency_industry_ratios.csv')
    #     execution_ratios = read_execution_ratios_from_csv(csv_filename)
    # elif industry == 'software development':
    #     csv_filename = os.path.join(os.path.dirname(__file__), 'hipe_site.csv')
    #     execution_ratios = read_execution_ratios_from_csv(csv_filename)
    # else:
    #     print("Invalid industry specified. Please use 'food' or 'resignation'.")
    #     return

    # # Example of getting IP address (can be a placeholder)
    # ip_address = "123.456.789.012"

    # Run the search based on the number of searches per day
    # random_num = random.randint(1, keyword_len)
    # keyword = keyword_list[random_num-1]
    # print(f"Index {random_num} Keyword Search {keyword}")
        
        # Step 1: Open Chrome with remote debugging enabled
    subprocess.Popen(r'"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" --remote-debugging-port=9222 --user-data-dir="C:\Chrome_debug"')
    pyautogui.moveTo(947, 1056, duration=1.5, tween=pyautogui.easeInOutQuad)  # Example coordinates for taskbar, change as needed
    pyautogui.click()
        # Open Chrome with remote debugging enabled
    open_chrome_with_debugging()

        # Attach Selenium to the Chrome instance
    driver = attach_selenium_to_chrome()
    driver.get("https://www.tripadvisor.com.ph/CreateListing.html")
        
    # google_results = search_google("TripAdvisor", driver)
    # clicked_link_google = click_link(google_results, driver)
    # driver.back()
    # save_searched_keyword(keyword, "Google", keyword, ip_address, "success" if google_results else "failed")

        # yahoo_results = search_yahoo(keyword, driver)
        # clicked_link_yahoo = click_link(yahoo_results, driver)
        # driver.back()
        # save_searched_keyword(keyword, "Yahoo", keyword, ip_address, "success" if clicked_link_yahoo else "failed")
        

        # After going back to the search results page, go to the next page
        # yahoo_results = click_next_page_yahoo(driver)
        # clicked_link_yahoo = click_link(yahoo_results, driver)
        # save_searched_keyword(keyword, "Google", keyword, ip_address, "success" if clicked_link_yahoo else "failed")
        

        # Close the browser
        # driver.quit()
    # pyautogui.moveTo(1897, 11, duration=1.5, tween=pyautogui.easeInOutQuad)  # Example coordinates for taskbar, change as needed
    #     pyautogui.click()

    # current_time = datetime.now()
    # sleep_interval = calculate_sleep_interval(current_time, searches_per_day, execution_ratios)
        # print(f"Sleeping for {sleep_interval:.2f} seconds before the next search...")
    print("Sleep at {1000} seconds")
    time.sleep(20)

if __name__ == "__main__":
    main()
