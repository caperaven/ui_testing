import time

from src.elements import get_element
from selenium.webdriver.support.ui import WebDriverWait
from src.data import data
from src.errors import set_error
from src.utils import get_name
from src.wait.conditions import _class_condition, _is_ready_condition, _attribute_condition, _css_condition, \
    _text_condition, _property_condition, _count_condition, _selected_condition, _element_condition, \
    _window_count_condition, _idle_condition


def wait_is_ready(driver, args, results):
    args["property"] = "isReady"

    element = get_element(driver, args, results)

    if element is None:
        return

    is_ready = element.get_property("isReady")

    if is_ready is not True:
        driver.execute_script(data["scripts"]["is_ready"].format(args["query"]))
        try:
            timeout = args["timeout"] if "timeout" in args else 5
            WebDriverWait(driver, timeout).until(_is_ready_condition(args, results))
            results[args["step"]] = "success"
        except Exception as e:
            print("wait_is_ready failed, {}".format(e.__class__.__name__))
            set_error(driver, results, args["step"], "error: timeout() - waiting for isReady on '{}', {}".format(args["query"], e.__class__.__name__))
            pass


def wait_for_element(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 30
        WebDriverWait(driver, timeout).until(_element_condition(args, results))
        results[args["step"]] = "success"
        return True
    except Exception as e:
        print("wait_for_element failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for element {}".format(name, e.__class__.__name__))
        return False
        pass


def wait_for_attribute(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_attribute_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_attribute failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for attribute on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_attributes(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 30
        attributes = args["attributes"].keys()

        for attribute in attributes:
            value = args["attributes"][attribute]
            args["attr"] = attribute
            args["value"] = value
            WebDriverWait(driver, timeout).until(_attribute_condition(args, results))

        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_attribute failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for attribute on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_css_property(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_css_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_css_property failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for css property on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_text(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_text_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_text failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for text on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_value(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        args["attr"] = "value"
        WebDriverWait(driver, timeout).until(_attribute_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_value failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for value on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_property(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_property_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_property failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_css_class(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_class_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_css_class failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_children(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        query = args["query"]
        args["query"] = "{} > *".format(query)
        WebDriverWait(driver, timeout).until(_count_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_children failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for children on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_count(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_count_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_count failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for count on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_time(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        time.sleep(timeout)
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_time failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for time '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_selected(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_selected_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_selected failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for selected on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_for_windows(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        WebDriverWait(driver, timeout).until(_window_count_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_for_selected failed, {}".format(e.__class__.__name__))
        name = get_name(args)
        set_error(driver, results, args["step"], "error: timeout() - waiting for selected on '{}', {}".format(name, e.__class__.__name__))
        pass


def wait_until_idle(driver, args, results):
    try:
        timeout = args["timeout"] if "timeout" in args else 5
        driver.execute_script(data["scripts"]["idle-false"])
        driver.execute_script(data["scripts"]["idle-true"])
        WebDriverWait(driver, timeout).until(_idle_condition(args, results))
        results[args["step"]] = "success"
    except Exception as e:
        print("wait_until_idle failed, {}".format(e.__class__.__name__))
        set_error(driver, results, args["step"], "error: timeout() - waiting for idle")
        pass
