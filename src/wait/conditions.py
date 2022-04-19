from selenium.webdriver.common.by import By
from src.elements import get_element


def _is_ready_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute("data-ready")
        if value is None:
            return False
        else:
            return True

    return _predicate


def _is_enabled_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute("disabled")
        return value is None

    return _predicate


def _text_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.text
        exp_value = args["value"]
        return value == exp_value

    return _predicate


def _attribute_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        value = element.get_attribute(args["attr"])
        exp_value = args["value"]
        return value == exp_value

    return _predicate


def _css_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        prop = args['property']
        value = element.value_of_css_property(prop)
        exp_value = args["value"]
        return value == exp_value

    return _predicate


def _property_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        prop = args["property"]
        value = element.get_property(prop)
        exp_value = args["value"]
        return value == exp_value

    return _predicate


def _class_condition(args, results):
    def _predicate(driver):
        element = get_element(driver, args, results)
        cls = element.get_attribute("class")
        sub = args["class"]
        return sub in cls
    return _predicate

def _child_count_condition(args, results):
    def _predicate(driver):
        query = args["query"]
        count = args["count"]
        all_children_by_css = driver.find_elements_by_css_selector(query)
        return len(all_children_by_css) == count
    return _predicate
