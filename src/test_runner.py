from selenium import webdriver
# actions
from src.actions.navigate import navigate
from src.actions.type import type_text
from src.actions.click import click
# assertions
from src.assertions.assert_value import assert_value_eq, assert_value_neq
from src.assertions.assert_attribute import assert_attr_eq, assert_attr_nq
# components
from src.wait.components import wait_is_ready

class TestRunner:
    def __init__(self, logger):
        self.logger = logger
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.quit()
        self.logger = None
        self.driver = None

    """
    run the given test's steps and update the results object
    """
    def run_test(self, json, results, file):
        self.logger.step(json["id"])

        test_results = results[json["id"]] = {
            "summary": {
                "file": file,
                "success": True,
                "error_count": 0
            }
        }

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
                else:
                    test_results[step_name] = "error: action '{}' not recognised".format(action)
                    test_results["summary"]["error_count"] = test_results["summary"]["error_count"] + 1

    def navigate(self, step, results):
        navigate(self.driver, step, results)

    def type_text(self, step, results):
        type_text(self.driver, step, results)

    def click(self, step, results):
        click(self.driver, step, results)

    def assert_value_eq(self, step, results):
        assert_value_eq(self.driver, step, results)

    def assert_value_neq(self, step, results):
        assert_value_neq(self.driver, step, results)

    def assert_attr_eq(self, step, results):
        assert_attr_eq(self.driver, step, results)

    def assert_attr_nq(self, step, results):
        assert_attr_nq(self.driver, step, results)

    def wait_is_ready(self, step, results):
        wait_is_ready(self.driver, step, results)
