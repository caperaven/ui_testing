import os


def print_screen(driver, args, results):
    parts = args["file"].split(":")

    part = None
    if len(parts) == 1:
        part = parts[0]
    else:
        part = parts[1]

    file = os.path.join(os.getcwd(), "test_results", part)
    print("saving screen: {}".format(file))
    driver.get_screenshot_as_file(file)
