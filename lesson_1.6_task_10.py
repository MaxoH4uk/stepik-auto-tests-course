from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    first_name = browser.find_element_by_xpath("//form/div[1]/div[1]/input")
    first_name.send_keys("John")
    last_name = browser.find_element_by_xpath("//form/div[1]/div[2]/input")
    last_name.send_keys("Doe")
    email = browser.find_element_by_xpath("//form/div[1]/div[3]/input")
    email.send_keys("johndoe@gmail.com")
    phone = browser.find_element_by_xpath("//form/div[2]/div[1]/input")
    phone.send_keys("33-33-33")
    address = browser.find_element_by_xpath("//form/div[2]/div[2]/input")
    address.send_keys("USA")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)
    browser.quit()