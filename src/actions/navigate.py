from src.data import data
from src.wait.components import wait_for_css_property, wait_for_attribute


def navigate(driver, args, results):
    driver.execute_script(data["scripts"]["idle-false"])
    url = args["url"]
    driver.get(url)

    wait_for_css_property(driver, {
        "query": "body",
        "property": "visibility",
        "value": "hidden",
        "eval": "ne",
        "step": "navigate"
    }, results)

    driver.execute_script(data["scripts"]["idle-true"])

    wait_for_attribute(driver, {
        "query": "body",
        "attr": "idle",
        "value": "true",
        "step": "navigate"
    }, results)
