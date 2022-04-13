from src.elements import get_element
from src.errors import set_error


def assert_text_eq(driver, args, results):
    element = get_element(driver, args, results)
    value = element.text
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = "success"
    else:
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: text on '{}' should have been '{}' but was '{}'".format(name, exp_value, value))


def assert_text_neq(driver, args, results):
    element = get_element(driver, args, results)
    value = element.text
    exp_value = args["value"]

    if value == exp_value:
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: text on '{}' should have been '{}' but was '{}'".format(name, exp_value, value))
    else:
        results[args["step"]] = "success"
