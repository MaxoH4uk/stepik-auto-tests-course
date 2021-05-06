from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/execute_script.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    peopleRule = browser.find_element_by_id("peopleRule")
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(y)
    browser.find_element_by_css_selector("input[type='checkbox']").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", peopleRule)
    browser.find_element_by_css_selector("input[value='robots']").click()
    browser.find_element_by_css_selector("button").click()
    alert = browser.switch_to_alert()
    print(alert.text)
    browser.quit()