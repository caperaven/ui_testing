from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def assert_value_eq(driver, args, results):
    element = None

    exp_value = args["value"]

    if "id" in args:
        element = driver.find_element(By.ID, args["id"])

    WebDriverWait(driver, 10).until(EC.visibility_of(element))

    value = element.get_attribute("value")
    if str(exp_value) == str(value):
        results[args["step"]] = "success"
    else:
        results[args["step"]] = "error: expected {} but found {}".format(exp_value, value)
