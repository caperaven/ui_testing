from src.errors import set_error


def refresh(driver, args, results):
    try:
        driver.refresh()
        results[args["step"]] = "success"
    except Exception as e:
        print(e)
        set_error(driver, results, args["step"], "error: refresh failed".format())
        pass