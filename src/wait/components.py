from src.elements import get_element, get_property
from selenium.webdriver.support.ui import WebDriverWait
from src.data import data
from src.errors import set_error


def _is_ready_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute("data-ready")
        if value is None:
            return False
        else:
            return True

    return _predicate


def wait_is_ready(driver, args, results):
    args["property"] = "isReady"
    is_ready = get_property(driver, args, results)

    if is_ready is True:
        return True
    else:
        driver.execute_script(data["scripts"]["is_ready"].format(args["query"]))
        try:
            timeout = args["timeout"] or 3
            WebDriverWait(driver, timeout).until(_is_ready_condition(args, results))
        except Exception:
            set_error(results, args["step"], "error: timeout({}) - waiting for '{}'".format(timeout, args["query"]))
            pass
        return True
