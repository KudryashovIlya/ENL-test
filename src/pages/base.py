from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf import URL, EMAIL, PASSWORD


class MainPage:

    def __init__(self):
        self.driver = webdriver.Chrome('/tmp/chromedriver')
        self.driver.implicitly_wait(500)

    def open(self, url=URL):
        self.driver.get(url)
        self.driver.find_element(By.XPATH, './/div[contains(@class,"flag")]/img').click()
        return self.driver

    def close(self):
        self.driver.close()

    def get_email(self):
        return self.driver.find_element(By.XPATH, './/input[contains(@data-role, "loginEmail")]')

    def get_pwd(self):
        return self.driver.find_element(By.XPATH, './/input[@name="password"]')

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, './/button[@data-role="loginHeaderButton"]')

    def get_submit_login(self):
        return self.driver.find_element(By.XPATH, './/button[@data-id="login-button"]')

    def get_url(self):
        return self.driver.current_url

    def get_error(self):
        return self.driver.find_elements(By.XPATH, './/div[contains(@class,"error")]')

    def get_dialog_window(self):
        return self.driver.find_element(By.XPATH,
                                        './/div[contains(@class,"dialog")]/div[contains(@class,"content")]')

    def get_result(self):
        """
        return count of game
        """
        return self.driver.find_element(By.XPATH, './/p[contains(@class,"result")]')

    def get_menu(self):
        return self.driver.find_element(By.XPATH, './/div[@data-role="openLeftSideMenu"]')

    def get_submenu(self, category):
        return self.driver.find_element(By.XPATH, f'.//a[@data-role="{category}"]')

    def login(self, user=EMAIL, password=PASSWORD, flag=0):
        """
        flag = 1: checking successful login
        flag = 0: do not checking successful login
        """
        login_but = self.get_login_button()
        login_but.click()

        email = self.get_email()
        pwd = self.get_pwd()
        submit = self.get_submit_login()

        email.send_keys(user)
        pwd.send_keys(password)
        submit.click()

        if flag:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/div[contains(@class, "dialog-close")]'))
                )
            finally:
                element.click()

    def search(self, category='', game_name=''):
        # sometimes need to refresh

        menu = self.get_menu()
        menu.click()

        submenu = self.get_submenu(category)
        submenu.click()

        search_b = self.driver.find_element(By.XPATH, './/div[contains(@class, "searchButton")]')
        search_b.click()

        input_s = self.driver.find_element(By.XPATH, './/input[@data-role="searchInput"]')
        input_s.click()
        input_s.send_keys(game_name)

    def launch(self):
        launch_g = self.driver.find_element(By.XPATH,
                                            './/div[@data-role="searchResult"]//div[contains(@class,"game")]')
        launch_g.click()

        self.driver.find_element(By.XPATH, './/button[@data-role="playForFunButton"]').click()
