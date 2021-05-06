from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
with webdriver.Chrome() as browser:
    browser.get(link)
    first_name = browser.find_element_by_name("first_name")
    first_name.send_keys("Maxim")
    last_name = browser.find_element_by_name("last_name")
    last_name.send_keys("Tikhomirov")
    city = browser.find_element_by_class_name("city")
    city.send_keys("Ivanovo")
    country = browser.find_element_by_id("country")
    country.send_keys("Russian Federation")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()
    time.sleep(15)
    browser.quit()