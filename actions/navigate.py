from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate(driver, **kwargs):
    url = kwargs["url"]
    driver.get(url)

    #element = driver.find_element(By.ID, kwargs["id"])
    return
