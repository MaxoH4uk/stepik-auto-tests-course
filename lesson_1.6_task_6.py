from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    inputs = browser.find_elements_by_css_selector("input")

    for input in inputs:
        input.send_keys("1")

    button = browser.find_element_by_css_selector("button")
    button.click()
    alert = browser.switch_to_alert
    print (alert.text)
    browser.quit()