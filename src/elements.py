from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.errors import set_error
from src.data import data


def get_element(driver, args, results):
    element = None
    name = ""

    try:
        if "id" in args:
            name = args["id"]
            element = driver.find_element(By.ID, name)

        if "query" in args:
            name = args["query"]
            if ":shadow:" in name:
                parts = name.split(":")
                parent = driver.find_element(By.CSS_SELECTOR, parts[0])
                element = parent.shadow_root.find_element(By.CSS_SELECTOR, parts[2])
            else:
                element = driver.find_element(By.CSS_SELECTOR, name)

        WebDriverWait(driver, 10).until(EC.visibility_of(element))

    except Exception:
        set_error(driver, results, args["step"], "error: element '{}' not found".format(name))
        pass

    if element is None:
        set_error(driver, results, args["step"], "error: element '{}' not found".format(name))

    return element