from selenium.webdriver.common.by import By


class SwagPage():
    def __init__(self, driver) -> None:
        self.d = driver
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_id = "login-button"

        self.burger_id = "react-burger-menu-btn"
        self.logout_btn = "logout_sidebar_link"

    def login_user(self, username, password):
        self.d.find_element(By.ID, self.username_id).clear()
        self.d.find_element(By.ID, self.password_id).clear()
        self.d.find_element(By.ID, self.username_id).send_keys(username)
        self.d.find_element(By.ID, self.password_id).send_keys(password)
        self.d.find_element(By.ID, self.login_id).click()

    def logout_user(self):
        self.d.find_element(By.ID, self.burger_id).click()
        self.d.find_element(By.ID, self.logout_btn).click()
