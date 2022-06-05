from selenium import webdriver


driver_path = r"C:\Users\death\Desktop\Projects\Github\code-bits\misc-files\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

test_url = "https://locations.lkqpickyourpart.com/ca/monrovia/3333-peck-road/"
name = None
inv_url = None
yardcode = None

# go to page
driver.get(test_url)

# find yard name
# class name = "LocationName-geo"
#name = driver.find_element_by_class_name("LocationName-geo").text
name = driver.find_element(By.,value="LocationName-geo").text
print(name)

# find inv url
# class name = "Product-linkWrapper"
inv_url = driver.find_element_by_link_text("View Our Inventory")
print(inv_url)











driver.quit()