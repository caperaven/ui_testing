def navigate(driver, args, results):
    url = args["url"]
    driver.get(url)

    results[args["step"]] = "success"
    return
