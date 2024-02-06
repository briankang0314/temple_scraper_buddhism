from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Setup WebDriver (Chrome in this example)
driver = webdriver.Chrome(executable_path='path_to_your_chromedriver')

# Open the webpage
driver.get('your_website_url')

# Wait for the page to load
time.sleep(5)

# Example loop to navigate through pagination
for i in range(1, 368):  # Assuming 367 pages
    # Find and click the pagination button
    # You might need to adjust the selector based on actual content
    next_page_button = driver.find_element(By.CSS_SELECTOR, f'a[data-param="all"][id="{i}"]')
    next_page_button.click()
    
    # Wait for the page to load
    time.sleep(5)
    
    # Now, extract the data from the page
    # Use driver.find_elements_by_xpath, driver.find_elements_by_css_selector, etc.
    
    # Example: Extracting temple names and addresses would go here
    # You would add the logic based on the page's HTML structure
    
    # Optionally, implement logic to click "다음" if necessary

# Remember to close the browser when done
driver.quit()