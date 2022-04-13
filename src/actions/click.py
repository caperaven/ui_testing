from src.elements import get_element
from selenium.webdriver.support.ui import WebDriverWait
from src.errors import set_error
from src.wait.conditions import _is_enabled_condition


def click(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    try:
        WebDriverWait(driver, 10).until(_is_enabled_condition(args, results))
        element.click()
        results[args["step"]] = "success"
    except Exception as e:
        print(e)
        set_error(results, args["step"], "error: element '{}' not clickable".format(args["id"] or args["query"]))
        pass
