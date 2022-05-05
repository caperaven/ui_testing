from src.elements import get_element
from selenium.webdriver.common.keys import Keys


def type_text(driver, args, results):
    value = args["value"]
    element = get_element(driver, args, results)

    if element is None:
        return

    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACK_SPACE)
    element.send_keys(value)
    element.send_keys(Keys.ENTER)
    results[args["step"]] = "success"
