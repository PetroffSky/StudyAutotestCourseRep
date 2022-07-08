from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import time
from math import log, sin


def robot(link):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # First part: explore correct (правильный) answer
    with webdriver.Chrome(options=options) as browser:
        browser.get(link[0])
        ''' First variant, use cycle:
        cost = browser.find_element(By.XPATH, "//h5[@id='price']").text        
        while cost != '$100':
            cost = browser.find_element(By.XPATH, "//h5[@id='price']").text
            if cost == '$100':
                browser.find_element(By.XPATH, "//button[@id='book']").click()
                break
        '''
        book_button = browser.find_element(By.XPATH, "//button[@id='book']")
        # In this stroke: Highlighting (подсветка) found elements in RED color:
        browser.execute_script("arguments[0].setAttribute('style', 'background-color: rgb(222, 0, 0);')", book_button)
        if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100')):
            book_button.click()
        check_number = int(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
        result = log(abs(12*sin(check_number)))
        input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
        input_field.click()
        input_field.send_keys(result)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        find_alert_window = browser.switch_to.alert
        text_on_alert_window = find_alert_window.text
        logger.info(text_on_alert_window)
        number = text_on_alert_window.split(': ')[1]
        logger.info(number)
        time.sleep(5)

    # Part two: sending correct answer in field on result
    with webdriver.Chrome(options=options) as browser:
        browser.get(link[1])
        time.sleep(10)
        login_email = browser.find_element(By.XPATH, "//form[@id='login_form']/div[@class='sign-form__input-group']/descendant::input[@name='login']")
        login_email.click()
        login_email.send_keys('ds9657@yandex.ru')
        login_pass = browser.find_element(By.XPATH, "//form[@id='login_form']/div[@class='sign-form__input-group']/descendant::input[@name='password']")
        login_pass.click()
        login_pass.send_keys('Petrchur_1')
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        browser.find_element(By.XPATH, "//button[@title='Продолжить обучение с последнего пройденного шага']").click()
        time.sleep(10)
        browser.execute_script("window.scrollBy(0, 120);")
        textfield = browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
        textfield.click()
        textfield.send_keys(number)
        browser.find_element(By.XPATH, "//button[text()='Отправить']").click()
        time.sleep(10)


def main():
    logger.info("Start of the work Robot!")
    robot(["http://suninjuly.github.io/explicit_wait2.html", "https://stepik.org/course/575/promo?auth=login"])
    logger.info("Robot work is Done!")


if __name__ == "__main__":
    main()

"""Методы из модуля expected_conditions:
Expected conditions Support
selenium.webdriver.support.expected_conditions.alert_is_present()
selenium.webdriver.support.expected_conditions.all_of(*expected_conditions)
An expectation that all of multiple expected conditions is true. 
Equivalent to a logical ‘AND’. Returns: When any ExpectedCondition 
is not met: False. When all ExpectedConditions are met: A List with 
each ExpectedCondition’s return value.

selenium.webdriver.support.expected_conditions.any_of(*expected_conditions)
An expectation that any of multiple expected conditions is true. 
Equivalent to a logical ‘OR’. Returns results of the first matching 
condition, or False if none do.

selenium.webdriver.support.expected_conditions.element_attribute_to_include(locator, attribute_)
An expectation for checking if the given attribute is included in 
the specified element. locator, attribute

selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be(locator, is_selected)
An expectation to locate an element and check if the selection 
state specified is in that state. locator is a tuple of 
(by, path) is_selected is a boolean

selenium.webdriver.support.expected_conditions.element_located_to_be_selected(locator)
An expectation for the element to be located is selected. locator 
is a tuple of (by, path)

selenium.webdriver.support.expected_conditions.element_selection_state_to_be(element, is_selected)
An expectation for checking if the given element is selected. 
element is WebElement object is_selected is a Boolean.

selenium.webdriver.support.expected_conditions.element_to_be_clickable(mark)
An Expectation for checking an element is visible and enabled 
such that you can click it.
element is either a locator (text) or an WebElement

selenium.webdriver.support.expected_conditions.element_to_be_selected(element)
An expectation for checking the selection is selected. element 
is WebElement object

selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it(locator)
An expectation for checking whether the given frame is available 
to switch to. If the frame is available it switches the given driver to the specified frame.

selenium.webdriver.support.expected_conditions.invisibility_of_element(element)
An Expectation for checking that an element is either invisible 
or not present on the DOM.

element is either a locator (text) or an WebElement

selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
An Expectation for checking that an element is either invisible 
or not present on the DOM.
locator used to find the element

selenium.webdriver.support.expected_conditions.new_window_is_opened(current_handles)
An expectation that a new window will be opened and have the number 
of windows handles increase

selenium.webdriver.support.expected_conditions.none_of(*expected_conditions)
An expectation that none of 1 or multiple expected conditions is true. 
Equivalent to a logical ‘NOT-OR’. Returns a Boolean

selenium.webdriver.support.expected_conditions.number_of_windows_to_be(num_windows)
An expectation for the number of windows to be a certain value.

selenium.webdriver.support.expected_conditions.presence_of_all_elements_located(locator)
An expectation for checking that there is at least one element present 
on a web page. locator is used to find the element returns the list of 
WebElements once they are located

selenium.webdriver.support.expected_conditions.presence_of_element_located(locator)
An expectation for checking that an element is present on the DOM of a 
page. This does not necessarily mean that the element is visible. 
locator - used to find the element returns the WebElement once it is located

selenium.webdriver.support.expected_conditions.staleness_of(element)
Wait until an element is no longer attached to the DOM. element is the 
element to wait for. returns False if the element is still attached 
to the DOM, true otherwise.

selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
An expectation for checking if the given text is present in the 
specified element. locator, text

selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_attribute(locator, attribute_, text_)
An expectation for checking if the given text is present in the 
element’s attribute. locator, attribute, text

selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_value(locator, text_)
An expectation for checking if the given text is present in the 
element’s value. locator, text

selenium.webdriver.support.expected_conditions.title_contains(title)
An expectation for checking that the title contains a case-sensitive 
substring. title is the fragment of title expected returns True 
when the title matches, False otherwise

selenium.webdriver.support.expected_conditions.title_is(title)
An expectation for checking the title of a page. title is the expected 
title, which must be an exact match returns True if the title matches, 
false otherwise.

selenium.webdriver.support.expected_conditions.url_changes(url)
An expectation for checking the current url. url is the expected url, 
which must not be an exact match returns True if the url is different, 
false otherwise.

selenium.webdriver.support.expected_conditions.url_contains(url)
An expectation for checking that the current url contains a 
case-sensitive substring. url is the fragment of url expected, 
returns True when the url matches, False otherwise

selenium.webdriver.support.expected_conditions.url_matches(pattern)
An expectation for checking the current url. pattern is the expected 
pattern, which must be an exact match returns True if the url matches, 
false otherwise.

selenium.webdriver.support.expected_conditions.url_to_be(url)
An expectation for checking the current url. url is the expected url, 
which must be an exact match returns True if the url matches, false 
otherwise.

selenium.webdriver.support.expected_conditions.visibility_of(element)
An expectation for checking that an element, known to be present on 
the DOM of a page, is visible. Visibility means that the element is 
not only displayed but also has a height and width that is greater 
than 0. element is the WebElement returns the (same) WebElement once it is visible

selenium.webdriver.support.expected_conditions.visibility_of_all_elements_located(locator)
An expectation for checking that all elements are present on the DOM 
of a page and visible. Visibility means that the elements are not only 
displayed but also has a height and width that is greater than 0. 
locator - used to find the elements returns the list of WebElements 
once they are located and visible

selenium.webdriver.support.expected_conditions.visibility_of_any_elements_located(locator)
An expectation for checking that there is at least one element visible 
on a web page. locator is used to find the element returns the list 
of WebElements once they are located

selenium.webdriver.support.expected_conditions.visibility_of_element_located(locator)
An expectation for checking that an element is present on the DOM of 
a page and visible. Visibility means that the element is not only 
displayed but also has a height and width that is greater than 0. 
locator - used to find the element returns the WebElement once it 
is located and visible
"""