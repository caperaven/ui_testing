from selenium import webdriver
from actions.navigate import navigate
from actions.type import type_text

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

        for step_name in json:
            if step_name == "id":
                continue

            step = json[step_name]
            action = step["action"]

            self_attr = getattr(self, action, None)
            if callable(self_attr):
                self_attr(step)


    def navigate(self, args):
        navigate(self.driver, args)

    def type_text(self, args):
        type_text(self.driver, args)



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from actions_map import actions
#
# driver = webdriver.Chrome()
# actions["navigate"](driver, url="http://127.0.0.1:8000/#mdc")
#
#
# # try:
# #     WebDriverWait(driver, 3).until(EC.visibility_of((By.TAG_NAME, "h2")))
# #     print("page is ready")
# # except TimeoutException:
# #     print("page timed out")
#
# driver.quit()
#
# ## Outstanding
# ## How do I debug my test.
# ## Result Log