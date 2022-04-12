from selenium import webdriver
from src.actions.navigate import navigate
from src.actions.type import type_text
from src.assertions.assert_value_eq import assert_value_eq

class TestRunner:
    def __init__(self, logger):
        self.logger = logger
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.quit()
        self.logger = None
        self.driver = None

    """
    fun the given test's steps and update the results object
    """
    def run_test(self, json, results):
        self.logger.step(json["id"])

        test_results = results[json["id"]] = {}

        for step_name in json:
            if step_name == "id":
                continue
            else:
                step = json[step_name]
                action = step["action"]
                step["step"] = step_name

                self_attr = getattr(self, action, None)
                if callable(self_attr):
                    self_attr(step, test_results)


    def navigate(self, step, results):
        navigate(self.driver, step, results)

    def type_text(self, step, results):
        type_text(self.driver, step, results)

    def assert_value_eq(self, step, results):
        assert_value_eq(self.driver, step, results)