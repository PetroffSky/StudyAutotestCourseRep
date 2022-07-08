import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger


@logger.catch
def robot(link):
    with webdriver.Chrome() as browser:
        browser.get(link)
        field_first_name = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
        field_first_name.click()
        field_first_name.send_keys("Igor")
        field_last_name = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
        field_last_name.click()
        field_last_name.send_keys("Petrov")
        field_email_name = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
        field_email_name.click()
        field_email_name.send_keys("igor@petrov.ru")
        load_file = browser.find_element(By.XPATH, "//input[@type='file']")
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'debug.txt')
        load_file.send_keys(file_path)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)


def main():
    robot("http://suninjuly.github.io/file_input.html")


if __name__ == "__main__":
    logger.info("Start is program!")
    main()
    logger.info("Program is Done!")



