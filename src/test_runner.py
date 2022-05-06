from selenium import webdriver
# actions
from src.actions.navigate import navigate
from src.actions.type import type_text
from src.actions.click import click, dbl_click, context_click
from src.actions.switch_to import switch_to_frame, switch_to_default, switch_to_tab
# assertions
from src.assertions.assert_value import assert_value_eq, assert_value_neq
from src.assertions.assert_attribute import assert_attr_eq, assert_attr_nq, assert_attributes
from src.assertions.assert_css import assert_style_eq, assert_style_neq
from src.assertions.assert_text import assert_text_eq, assert_text_neq
from src.assertions.assert_property import assert_property_eq, assert_property_neq
from src.assertions.assert_tag_name import assert_tag_name_eq, assert_tag_name_neq
from src.assertions.assert_child_count import assert_child_count_eq, assert_child_count_neq
# components
from src.wait.components import wait_for_css_class, wait_is_ready, wait_for_attribute, wait_for_css_property, wait_for_text, \
    wait_for_property, wait_for_children, wait_for_selected, wait_for_time, wait_for_count, wait_for_value, wait_for_element
import sys


class TestRunner:
    def __init__(self, logger):
        self.logger = logger

        options = None
        if sys.argv.__contains__("--debug"):
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("-disable-extensions")
            options.add_argument("--auto-open-devtools-for-tabs")

        self.driver = webdriver.Chrome(options=options)

    def __del__(self):
        self.driver.quit()
        self.logger = None
        self.driver = None

    """
    run the given test.json's steps and update the results object
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
            if step_name == "id" or "skip." in step_name:
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

        if "--root" in sys.argv:
            index = sys.argv.index("--root")
            url = sys.argv[index + 1]
            self.navigate({
                "step": "go to root",
                "url": url
            }, test_results)

    def navigate(self, step, results):
        navigate(self.driver, step, results)

    def type_text(self, step, results):
        type_text(self.driver, step, results)

    def click(self, step, results):
        click(self.driver, step, results)

    def dbl_click(self, step, results):
        dbl_click(self.driver, step, results)

    def context_click(self, step, results):
        context_click(self.driver, step, results)

    def switch_to_frame(self, step, results):
        switch_to_frame(self.driver, step, results)

    def switch_to_default(self, step, results):
        switch_to_default(self.driver, step, results)

    def switch_to_tab(self, step, results):
        switch_to_tab(self.driver, step, results)

    def assert_value_eq(self, step, results):
        assert_value_eq(self.driver, step, results)

    def assert_value_neq(self, step, results):
        assert_value_neq(self.driver, step, results)

    def assert_attr_eq(self, step, results):
        assert_attr_eq(self.driver, step, results)

    def assert_attr_nq(self, step, results):
        assert_attr_nq(self.driver, step, results)

    def assert_attributes(self, step, results):
        assert_attributes(self.driver, step, results)

    def wait_for_element(self, step, results):
        wait_for_element(self.driver, step, results)

    def wait_is_ready(self, step, results):
        wait_is_ready(self.driver, step, results)

    def wait_for_attribute(self, step, results):
        wait_for_attribute(self.driver, step, results)

    def wait_for_css_property(self, step, results):
        wait_for_css_property(self.driver, step, results)

    def wait_for_text(self, step, results):
        wait_for_text(self.driver, step, results)

    def wait_for_value(self, step, results):
        wait_for_value(self.driver, step, results)

    def wait_for_property(self, step, results):
        wait_for_property(self.driver, step, results)

    def wait_for_css_class(self, step, results):
        wait_for_css_class(self.driver, step, results)

    def wait_for_children(self, step, results):
        wait_for_children(self.driver, step, results)

    def wait_for_selected(self, step, results):
        wait_for_selected(self.driver, step, results)

    def wait_for_time(self, step, results):
        wait_for_time(self.driver, step, results)

    def wait_for_count(self, step, results):
        wait_for_count(self.driver, step, results)

    def assert_style_eq(self, step, results):
        assert_style_eq(self.driver, step, results)

    def assert_style_neq(self, step, results):
        assert_style_neq(self.driver, step, results)

    def assert_text_eq(self, step, results):
        assert_text_eq(self.driver, step, results)

    def assert_text_neq(self, step, results):
        assert_text_neq(self.driver, step, results)

    def assert_property_eq(self, step, results):
        assert_property_eq(self.driver, step, results)

    def assert_property_neq(self, step, results):
        assert_property_neq(self.driver, step, results)

    def assert_tag_name_eq(self, step, results):
        assert_tag_name_eq(self.driver, step, results)

    def assert_tag_name_neq(self, step, results):
        assert_tag_name_neq(self.driver, step, results)

    def assert_child_count_eq(self, step, results):
        assert_child_count_eq(self.driver, step, results)

    def assert_child_count_neq(self, step, results):
        assert_child_count_neq(self.driver, step, results)