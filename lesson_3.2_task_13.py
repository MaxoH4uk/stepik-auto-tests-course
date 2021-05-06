from selenium import webdriver
import time
import unittest

class TestRemake(unittest.TestCase):
    def test_firstLink(self):
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
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error! Text must be 'Congratulations! You have successfully registered!'")
            browser.quit()

    def test_secondLink(self):
        link = "http://suninjuly.github.io/registration2.html"
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
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error! Text must be 'Congratulations! You have successfully registered!'")
            browser.quit()

if __name__ == "__main__":
    unittest.main()