from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element_by_css_selector("button")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    input_value = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    browser.find_element_by_id("solve").click()
    answer_field.get_attribute()
    print(browser.switch_to.alert.text)
    browser.quit()