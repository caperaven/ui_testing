from src.elements import get_element
from selenium.webdriver.common.keys import Keys
import time

def type_text(driver, args, results):
    value = args["value"]
    element = get_element(driver, args, results)

    if element is None:
        return

    element.clear()
    element.send_keys(Keys.CONTROL + "a")
    time.sleep(0.2)
    element.send_keys(Keys.BACK_SPACE)
    time.sleep(0.2)
    element.send_keys(value)
    time.sleep(0.2)
    element.send_keys(Keys.ENTER)
    results[args["step"]] = "success"
