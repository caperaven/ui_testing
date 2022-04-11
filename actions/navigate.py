def navigate(driver, args, results):
    url = args["url"]
    driver.get(url)

    # element = driver.find_element(By.ID, kwargs["id"])

    results[args["step"]] = "success"
    return
