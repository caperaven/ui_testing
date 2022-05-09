from src.data import data
from src.wait.components import wait_for_css_property, wait_for_attribute
from src.errors import set_error


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


def close_window(driver, args, results):
    try:
        index = args["index"]

        if index == "last":
            index = len(driver.window_handles) - 1

        driver.switch_to.window(driver.window_handles[index])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        results[args["step"]] = "success"
    except Exception as e:
        print(e)
        set_error(driver, results, args["step"], "error: could not close window at ({})".format(index))
        pass
