from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def assert_value_eq(driver, **kwargs):
    element = None

    exp_value = kwargs["value"]

    if "id" in kwargs:
        element = driver.find_element(By.ID, kwargs["id"])

    WebDriverWait(driver, 10).until(EC.visibility_of(element))

    value = element.get_attribute("value")
    return exp_value == value