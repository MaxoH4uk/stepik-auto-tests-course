from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = int(num1) + int(num2)
    dropdown = Select(browser.find_element_by_id("dropdown"))
    dropdown.select_by_value(str(sum))
    browser.find_element_by_css_selector("button").click()
    alert = browser.switch_to_alert()
    print(alert.text)
    time.sleep(10)
    browser.quit()