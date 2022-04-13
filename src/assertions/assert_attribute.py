from src.elements import get_element
from src.errors import set_error


def assert_attr_eq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])
    exp_value = args["value"]

    if value == exp_value:
        results[args["step"]] = "success"
    else:
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: attribute '{}' on '{}' should have been '{}' but was '{}'".format(args["attr"], name, exp_value, value))


def assert_attr_nq(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    value = element.get_attribute(args["attr"])
    exp_value = args["value"]

    if value == exp_value:
        name = args["id"] or args["query"]
        set_error(results, args["step"], "error: attribute '{}' on '{}' should NOT have been '{}'".format(args["attr"], name, exp_value))
    else:
        results[args["step"]] = "success"
