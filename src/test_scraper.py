from src.elements import get_element
from selenium.webdriver.common.by import By


class TestScraper:
    def __init__(self):
        self.args = None
        self.path = None
        self.results = None

    def run(self, driver, args, results):
        self.args = args
        start = args["query"]
        self.path = [start]
        self.results = []
        element = get_element(driver, args, results)
        self.validate_element(element)

        if len(self.results) == 0:
            results[args["step"]] = "success"
        else:
            results[args["step"]] = self.results

        self.args = None
        self.path = None
        self.results = None

    def validate_element(self, element):
        if should_have_id(element):
            element_id = str(element.get_attribute("id"))
            data_id = str(element.get_attribute("data-id"))

            if (len(element_id) == 0 or element_id == "None") and (len(data_id) == 0 or data_id == "None"):
                self.results.append(' '.join(self.path))
        else:
            self.validate_children(element)

    def validate_children(self, element):
        children = element.find_elements(By.CSS_SELECTOR, "*")

        index = 0
        for child in children:
            self.path.append("{} - nth({})".format(child.tag_name, index))
            self.validate_element(child)
            del self.path[-1]
            index += 1
        pass


required_tag_names = ["input", "button", "select", "ul", "textarea"]

roles = [
    "menuitem",
    "scrollbar",
    "searchbox",
    "separator",
    "slider",
    "spinbutton",
    "switch",
    "tab",
    "tabpanel",
    "treeitem",
    "combobox",
    "menu",
    "menubar",
    "cell",
    "columnheader",
    "row",
    "listitem",
    "button",
    "checkbox",
    "gridcell",
    "link",
    "menuitem",
    "menuitemcheckbox",
    "menuitemradio",
    "option",
    "radio",
    "textbox"]


def should_have_id(element):
    if required_tag_names.__contains__(element.tag_name):
        return True

    if element.tag_name.__contains__("button"):
        return True

    tab_index = element.get_attribute("tabindex")
    if tab_index == 0 or tab_index == -1:
        return True

    role = element.get_attribute("role")
    if roles.__contains__(role):
        return True

    return False

