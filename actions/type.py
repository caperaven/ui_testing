from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def type_text(driver, args):
    element = None

    value = args["value"]
    if "id" in args:
        element = driver.find_element(By.ID, args["id"])
    elif "query" in args:
        element = driver.find_element(By.CSS_SELECTOR, args["query"])

    WebDriverWait(driver, 10).until(EC.visibility_of(element))
    element.send_keys(value)
