import time

from src.errors import set_error
from src.elements import get_element
from src.utils import get_name


def switch_to_frame(driver, args, results):
    element = get_element(driver, args, results)

    if element is None:
        return

    try:
        driver.switch_to.frame(element)
    except Exception as e:
        print(e)
        name = get_name(args)
        set_error(driver, results, args["step"], "error: could not switch to frame '{}'".format(name))
        pass


def switch_to_default(driver, args, results):
    try:
        driver.switch_to.default_content()
    except Exception as e:
        print(e)
        set_error(driver, results, args["step"], "error: could not switch to default content")
        pass


def switch_to_tab(driver, args, results):
    try:
        time.sleep(1)
        index = args["index"]
        driver.switch_to.window(driver.window_handles[index])
    except Exception as e:
        print(e)
        set_error(driver, results, args["step"], "error: could not swap to tab ({})".format(index))
        pass
