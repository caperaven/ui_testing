from src.wait.components import wait_for_css_property

def navigate(driver, args, results):
    url = args["url"]
    driver.get(url)

    args["query"] = "body"
    args["property"] = "visibility"
    args["value"] = "hidden"
    args["eval"] = "ne"

    wait_for_css_property(driver, args, results)