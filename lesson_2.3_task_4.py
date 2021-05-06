from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element_by_css_selector("button").click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    browser.find_element_by_css_selector("button").click()
    print(browser.switch_to.alert.text)
    browser.quit()
