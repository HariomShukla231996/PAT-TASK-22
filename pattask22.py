from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Set up the browser (you may need to specify the path to your webdriver executable)
driver = webdriver.Chrome()

# Open the URL
url = "https://jqueryui.com/droppable/"
driver.get(url)


# Locate the draggable and droppable elements
draggable_element = driver.find_element(By.XPATH, "//*[@id ='draggable']")
droppable_element = driver.find_element(By.XPATH, "This element is in iframe - //div[@id='droppable']")

# Use ActionChains to perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Close the browser window (optional)
driver.quit()