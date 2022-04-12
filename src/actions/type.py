from src.elements import get_element


def type_text(driver, args, results):
    value = args["value"]
    element = get_element(driver, args, results)
    element.send_keys(value)
    results[args["step"]] = "success"
