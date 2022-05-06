import os


def print_screen(driver, args, results):
    parts = args["file"].split(":")
    file = os.path.join(os.getcwd(), "test_results", parts[1])
    print("saving screen: {}".format(file))
    driver.get_screenshot_as_file(file)
