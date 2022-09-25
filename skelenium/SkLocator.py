# LOCATOR

# This file will define all of the necessary functions, classes and values required to set up a locator for
# a test case

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

Condition_names = [
    "Element to be Clickable",
    "Element to be Visible",
    "Element to be Present",
    "Element to be Selectable"
]

Identifier_names = [
    "XPATH",
    "ID",
    "Class Name"
]

# Use these values for cond
class Conditions:
    ElementClickable = 0
    ElementVisible = 1
    ElementPresent = 2
    ElementSelectable = 3


# Use these values for by
class Identifier:
    XPath = 0
    ID = 1
    ClassName = 2


# LOCATOR
# This class represents all of the data required to find an element on the screen
class SkLocator:
    conditions = [
        EC.element_to_be_clickable,
        EC.visibility_of_all_elements_located,
        EC.presence_of_all_elements_located,
        EC.element_located_to_be_selected
    ]

    ids = [
        By.XPATH,
        By.ID,
        By.CLASS_NAME
    ]

    # Set up the values needed to find an element
    # by - The identifier used to find the element
    # cond - how the element should appear on the screen
    # value - a value to test against our identifier
    # exc - Will this throw an exception if the element is not found?
    def __init__(self, cond, by, value, url, exc=False):
        self.by = by
        self.url = url
        self.value = value
        self.cond = cond
        self.exc = exc

    # COND TO EC
    # converts the classes above to something compatible with selenium and returns that expected condition
    def cond_to_ec(self):
        return self.conditions[self.cond]

    # ID TO BY
    def id_to_by(self):
        return self.ids[self.by]

    def print_ec(self):
        print(Condition_names[self.cond])

    def print_by(self):
        print(Identifier_names[self.by])

    # EC
    # executes the expected condition on the locator and returns the result
    def ec(self):
        if (self.cond is not None) and (self.exc is not None):
            return self.cond_to_ec()((
                self.id_to_by(),
                self.value
            ))

        print("Locator is not fully formed")
