from selenium import webdriver

chrome_driver_path = "D:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

###########################  USEFUL METHODS  ##############################
# driver.find_element_by_id
# driver.find_element_by_class_name
# driver.find_element_by_name
# To access the attributes of a driver object we can use .
# search_bar = driver.find_element_by_name("q")
# info = search_bar.get_attribute("placeholder")
# price = driver.find_element_by_id("id_name")
# print(price.text)
# doc_link = driver.find_element_by_css_selector("selectors_go here")
# driver.find_element_by_xpath("path_here") THIS WILL ALWAYSSSS WORK
# driver.find_element_by_link_text("link_text_here") this is for hyperlinks
#
# Remember that all of these finds have elements versions
# that give you a list instead of the first thing
###########################################################################

event_dates = [event.get_attribute("datetime").split("T")[0] for event in
               driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery .menu li time")]
event_names = [event.text for event in
               driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery .menu li a")]
events = {index: {"time": event_date, "name": event_name} for index, event_date, event_name in zip(range(len(event_dates)), event_dates, event_names)}
print(events)

# driver.close() closes the tab
driver.quit()  # closes the browser
