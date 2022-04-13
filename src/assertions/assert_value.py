from src.elements import get_value
from src.errors import set_error


def assert_value_eq(driver, args, results):
    exp_value = args["value"]
    value = get_value(driver, args, results)

    if value is None:
        return

    if str(exp_value) == str(value):
        results[args["step"]] = "success"
    else:
        set_error(results, args["step"], "error: expected {} but found {}".format(exp_value, value))


def assert_value_neq(driver, args, results):
    exp_value = args["value"]
    value = get_value(driver, args, results)

    if value is None:
        return

    if str(exp_value) == str(value):
        set_error(results, args["step"], "error: value should not be {}".format(value))
    else:
        results[args["step"]] = "success"


def assert_css_property_eq(driver, args, results):
    return


def assert_css_property_nq(driver, args, results):
    return
