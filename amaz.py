from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode, i.e., without a visible GUI

# Set up the WebDriver
driver = webdriver.Chrome("path/to/chromedriver", options=chrome_options)


product_url = "https://www.amazon.com/product-page"
driver.get(product_url)


see_all_reviews_button = driver.find_element_by_id("see-all-reviews-link")
see_all_reviews_button.click()


reviews = driver.find_elements_by_class_name("review-text")

for review in reviews:
    review_text = review.text
    print(review_text)


driver.quit()
