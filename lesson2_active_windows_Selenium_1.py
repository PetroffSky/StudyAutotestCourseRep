from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger
from math import sin, log
import time



@logger.catch
def robot(link):
    with webdriver.Chrome() as browser:
        browser.get(link[0])
        browser.find_element(By.XPATH, "//button[@type='submit']").click()  # Finder button on first page and clicker
        '''
        Теперь рассмотрим ситуацию, когда в сценарии теста возникает 
        необходимость не только получить содержимое alert, но и нажать 
        кнопку OK, чтобы закрыть alert. 
        Alert является модальным окном: 
        это означает, что пользователь не может взаимодействовать дальше 
        с интерфейсом, пока не закроет alert. Для этого нужно сначала 
        переключиться на окно с alert, а затем принять его с помощью 
        команды accept():        
        alert = browser.switch_to.alert
        alert.accept()
        Чтобы получить текст из alert, используйте свойство text объекта alert:
        alert = browser.switch_to.alert
        alert_text = alert.text
        '''
        find_alert_window = browser.switch_to.alert
        logger.info(find_alert_window.text)  # Get text from modal window
        find_alert_window.accept()  # Press button for confirm (подтверждаем) agreement
        find_number = int(browser.find_element(By.XPATH, "//span[@id='input_value']").text)
        result = log(abs(12*sin(find_number)))
        browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(result)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)  # Giving time for JS to finish
        find_alert_window_2 = browser.switch_to.alert  # Find second pop-up window
        logger.info(find_alert_window_2.text)
        number = str(find_alert_window_2.text).split(': ')[1]  # Get text from pop-up window
        logger.info(number)  # Get our answer from pop-up window
        find_alert_window_2.accept()
        # time.sleep(5)

    with webdriver.Chrome() as browser:
        browser.get(link[1])
        time.sleep(10)
        login_email = browser.find_element(By.XPATH, "//form[@id='login_form']/div[@class='sign-form__input-group']/descendant::input[@name='login']")
        login_email.click()
        login_email.send_keys('YOU_MAIL')
        login_pass = browser.find_element(By.XPATH, "//form[@id='login_form']/div[@class='sign-form__input-group']/descendant::input[@name='password']")
        login_pass.click()
        login_pass.send_keys('YOU_PASS')
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
    robot(["http://suninjuly.github.io/alert_accept.html",
           "https://stepik.org/course/575/promo?auth=login"])


if __name__ == "__main__":
    logger.info('Program is start!')
    main()
    logger.info('Program is Done!')