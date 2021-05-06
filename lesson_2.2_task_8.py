from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    first_name = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]")
    first_name.send_keys("Maxim")
    last_name = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]")
    last_name.send_keys("Tikhomirov")
    email = browser.find_element_by_xpath("/html/body/div[1]/form/div/input[3]")
    email.send_keys("maxim@gmail.com")
    file = browser.find_element_by_id("file")
    file.send_keys("C:/Users/mtikhomirov/Desktop/sad.txt")
    browser.find_element_by_css_selector("button").click()
    alert = browser.switch_to.alert
    print(alert.text)
    browser.quit()