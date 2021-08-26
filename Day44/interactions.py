from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_articles = driver.find_element_by_css_selector("#articlecount a")

# clicking links
num_articles.click()

# typing
search = driver.find_element_by_name("search")
search.send_keys("Python")
# clicking after typing
search.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit = driver.find_element_by_class_name("btn.btn-lg.btn-primary.btn-block")

first_name.send_keys("Uzair Tahamid")
last_name.send_keys("Siam")
email.send_keys("uzairt321@yahoo.com")
submit.send_keys(Keys.ENTER)

# driver.quit()
