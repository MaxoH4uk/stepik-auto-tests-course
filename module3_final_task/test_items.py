import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_search_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button'), "Can't find button"
