from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def type_text(driver, **kwargs):
    element = None

    value = kwargs["value"]
    if "id" in kwargs:
        element = driver.find_element(By.ID, kwargs["id"])
    elif "query" in kwargs:
        element = driver.find_element(By.CSS_SELECTOR, kwargs["query"])

    WebDriverWait(driver, 10).until(EC.visibility_of(element))
    element.send_keys(value)
