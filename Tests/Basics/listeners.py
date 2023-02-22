
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class Listener(AbstractEventListener):
    def before_navigate_to(self, url: str, driver) -> None:
        print(f"Before Navigate to: {url}")

    def after_navigate_to(self, url: str, driver) -> None:
        print(f"After Navigate to: {url}")

    def before_click(self, element, driver) -> None:
        print(f"Before clicking on: {element.text}")

    def after_click(self, element, driver) -> None:
        print(f"After clicking on: {element.text}")

    def before_close(self, driver) -> None:
        print(f"Before closing: {driver.title}")

    def after_close(self, driver) -> None:
        print(f"After closing")
