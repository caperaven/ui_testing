from src.elements import get_element
from src.errors import set_error


def assert_property_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    prop = args["property"]
    value = element.get_property(prop)
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = "success"
    else:
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: property '{}' on '{}' should have been '{}' but was '{}'".format(prop, name, exp_value, value))


def assert_property_neq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    prop = args["property"]
    value = element.get_property(prop)
    exp_value = args["value"]

    if value == exp_value:
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: property '{}' on '{}' should have been '{}' but was '{}'".format(prop, name, exp_value, value))
    else:
        results[args["step"]] = "success"
