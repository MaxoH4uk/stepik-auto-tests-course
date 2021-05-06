from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobut = browser.find_element_by_id("robotsRule")
    radiobut.click()
    button = browser.find_element_by_css_selector("button")
    button.click()
    alert = browser.switch_to_alert()
    print(alert.text)
    browser.quit()