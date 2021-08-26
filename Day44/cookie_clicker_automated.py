from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

store_items = driver.find_elements_by_css_selector("#store div b")
prices = [int(price.text.split(" - ")[1].replace(',', "")) for price in store_items[:-1]]
# items = [item.text.split(" - ")[0] for item in store_items[:-1]]
items = [item for item in store_items[:-1]]
item_prices = {item: price for item, price in zip(items, prices)}
print(item_prices)

while True:
    my_money = int(driver.find_element_by_id("money").text.replace(",", ""))
    cookie.click()
    for item in item_prices:
        if item_prices[item] < my_money:
            item.click()
    print(my_money)
