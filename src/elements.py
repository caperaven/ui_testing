from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.errors import set_error


def get_element(driver, args, results):
    element = None
    name = ""

    try:
        if "id" in args:
            name = args["id"]
            element = driver.find_element(By.ID, name)

        if "query" in args:
            name = args["query"]
            element = driver.find_element(By.CSS_SELECTOR, name)

        WebDriverWait(driver, 10).until(EC.visibility_of(element))

    except Exception:
        set_error(results, args["step"], "error: element '{}' not found".format(name))
        pass

    return element


def get_value(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return None

    return element.get_attribute("value")


def get_css_property_value(driver, args, results):
    element = get_element(driver, args, results)
    prop = args["property"]
    return element.value_of_css_property(prop)


def get_property(driver, args, results):
    element = get_element(driver, args, results)
    prop = args["property"]
    return element.get_property(prop)
