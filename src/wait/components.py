from src.elements import get_element
from selenium.webdriver.support.ui import WebDriverWait
from src.data import data
from src.errors import set_error
from src.wait.conditions import _is_ready_condition, _attribute_condition


def wait_is_ready(driver, args, results):
    args["property"] = "isReady"

    element = get_element(driver, args, results)

    if element is None:
        return

    is_ready = element.get_property("isReady")

    if is_ready is not True:
        driver.execute_script(data["scripts"]["is_ready"].format(args["query"]))
        try:
            timeout = args["timeout"] if "timeout" in args else 10
            WebDriverWait(driver, timeout).until(_is_ready_condition(args, results))
        except Exception:
            set_error(results, args["step"], "error: timeout() - waiting for '{}'".format(args["query"]))
            pass

    results[args["step"]] = "success"


"""
wait for an element's attribute to be there or not be there with a particular value
"""


def wait_for_attribute(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 10
        WebDriverWait(driver, timeout).until(_attribute_condition(args, results))
    except Exception as e:
        print(e)
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: timeout() - waiting for '{}'".format(name))
        pass

    results[args["step"]] = "success"

"""
wait for a css property to have a particular value
"""


def wait_for_css_property(driver, args, results):
    return


"""
wait for a css property to have a value
"""


def wait_for_css_class(driver, args, result):
    return


"""
use this for any complex type for example testing not operations
"""


def wait_for_css_selector(driver, args, result):
    return


"""
wait for a element to have child elements
"""


def wait_for_children(driver, args, results):
    return


"""
wait until a property on a element has a particular value
"""


def wait_for_property(driver, args, results):
    return
