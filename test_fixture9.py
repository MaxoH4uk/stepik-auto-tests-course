import time
import math
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCorrectAnswer():

    final_text = ""
    list = ["236895", "236896", "236897", "236898",
            "236899","236903", "236904", "236905"
           ]

    @pytest.mark.parametrize("task", list)
    def test_answer_equal_correct(self, browser, task):
        link = f"https://stepik.org/lesson/{task}/step/1"
        browser.get(link)
        answer_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
        answer = str(math.log(int(time.time())))
        answer_field.send_keys(answer)
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()
        correct_answer = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        assert correct_answer.text == "Correct!", f"{self.final_text.join(correct_answer.text)}"

