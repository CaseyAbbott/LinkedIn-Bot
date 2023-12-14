from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to the ChromeDriver executable
chrome_driver_path = '/home/user1/Documents/Casey/Dev/Drivers/chromedriver'

# Create ChromeOptions object and set the executable_path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--webdriver.chrome.driver={chrome_driver_path}')

# Create a new instance of the Chrome driver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://linkedin.com")

# Wait for the page to load
time.sleep(20)

# Find the username and password fields using WebDriverWait for better synchronization
try:
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_password")))

    # Enter the username and password
    username_field.send_keys("caseyabbott90@gmail.com")
    password_field.send_keys("yK2EYNQsosPjLFWaAxRk")

    # Click the login button
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-in-form__submit-btn--full-width")))
    submit.click()
    try:
        # Wait for the URL to change after login
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

        # Check if the new URL indicates a successful login (modify as needed)
        if "linkedin.com/feed/" in driver.current_url:
            print("Login successful. Current URL:", driver.current_url)
        else:
            raise Exception("Unexpected URL after login")

    except Exception as e:
        print(f"An error occurred: {e}")
    # Uncomment the next line if you want to print the current URL even on timeout
    # print("Current URL:", driver.current_url)

    try:
        # Wait for the page to fully load after login (you can adjust the timeout if needed)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='nav-typeahead-wormhole']")))
        # Print the current URL for verification
        print("Login successful. Current URL:", driver.current_url)
    except Exception as e:
        print(f"An error occurred while waiting for page to fully load after login: {e}")
        # Uncomment the next line if you want to print the current URL even on timeout
        # print("Current URL:", driver.current_url)

    try:
        # Wait for the login process to complete
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

        # Print the current URL for verification
        print("Login successful. Current URL:", driver.current_url)

        # Find and click the search icon
        search_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//svg[@data-test-icon='search-medium']")))
        search_icon.click()

        # Add a delay to allow the page to fully load after clicking the search icon
        time.sleep(5)  # Adjust the sleep duration as needed

        # Wait for the search bar to appear
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search']")))

        # Perform a sample search (replace 'example' with your actual search query)
        search_bar.send_keys("example")
        search_bar.send_keys(Keys.RETURN)

        # Wait for the search results page to load
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

        # Print the current URL after the search
        print("Search results page URL:", driver.current_url)

    except Exception as e:
        print(f"An error occurred: {e}")


finally:
    # Keep the browser window open
    input("Press Enter to close the browser window.")
    # Close the browser
    driver.quit()



