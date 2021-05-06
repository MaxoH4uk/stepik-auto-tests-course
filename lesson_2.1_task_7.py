from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobut = browser.find_element_by_id("robotsRule")
    radiobut.click()
    button = browser.find_element_by_css_selector("button")
    button.click()
    alert = browser.switch_to_alert()
    print(alert.text)
    browser.quit()