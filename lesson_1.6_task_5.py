from selenium import webdriver
import math, time

link = "http://suninjuly.github.io/find_link_text"
with webdriver.Chrome() as browser:
    browser.get(link)
    search_link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    search_link.click()
    first_name = browser.find_element_by_name("first_name")
    first_name.send_keys("Maxim")
    last_name = browser.find_element_by_name("last_name")
    last_name.send_keys("Tikhomirov")
    city = browser.find_element_by_class_name("city")
    city.send_keys("Ivanovo")
    country = browser.find_element_by_id("country")
    country.send_keys("Russian Federation")
    button = browser.find_element_by_css_selector("button")
    button.click()
    time.sleep(30)
    browser.quit()