# SK DRIVER

# This handles all of the operations required to manipulate the web site. These functions handle all of the waiting
# that the test will need to do as well.

from datetime import datetime as dt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions as exc

from skelenium import SkTags
from skelenium import SkGlobals as Gbs


# COMPARE PAGE
# compare the values of all elements and returns whether or not they are equal
def compare_page(one, two):
    for element1, element2 in zip(one, two):
        if not ec.visibility_of_element_located(element1) and not ec.visibility_of_element_located(element2):
            example = ec.visibility_of_element_located(element1)
            return False

    return True


# SK DRIVER
# This class handles manipulating the web browser
class SkDriver:
    def __init__(self, driver, account):
        self.target = None
        self.account = account
        self.__locators__ = {}

        if driver == SkTags.FIREFOX:
            self.driver = webdriver.Firefox(executable_path=Gbs.paths[driver])

        if driver == SkTags.EDGE:
            self.driver = webdriver.Edge(executable_path=Gbs.paths[driver])

        if driver == SkTags.CHROME:
            self.driver = webdriver.Chrome(executable_path=Gbs.paths[driver])

        if driver == SkTags.OPERA:
            self.driver = webdriver.Opera(executable_path=Gbs.paths[driver])

        if driver == SkTags.SAFARI:
            self.driver = webdriver.Safari(executable_path=Gbs.paths[driver])

    def __print_locators__(self):
        for locator, value in self.__locators__.items():
            print(value.url + " - " + locator + ":")
            print("_" * 4, end="")
            print("Identified By: ", end="")
            value.print_by()
            print("_" * 4, end="")
            print("Expected Condition: ", end="")
            value.print_ec()
            print("_" * 4, end="")
            print("Value: " + value.value)
            print("_")

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def write_to_target(self, input):
        target = self.driver.find_element(self.target.id_to_by(), self.target.value)
        target.send_keys(input)

    def click(self):
        target = self.driver.find_element(self.target.id_to_by(), self.target.value)
        target.click()

    # SET TARGET
    # set the object that the driver will be working with next
    def set_target(self, title, locator):
        self.target = locator
        self.__locators__[title] = locator

    # LOAD TARGET
    # A very simple load function that will attempt to load the webpage that your target is on for you
    def load_target(self):
        if self.driver.current_url != self.target.url:
            self.driver.get(self.target.url)

        try:
            WebDriverWait(self.driver, 10).until(self.target.ec())
        except exc.TimeoutException as e:
            print("Time out exception")
            raise e

    def get(self, url):
        self.driver.get(url)

    # FULL LOAD
    # get a website and wait until there are no longer any changes occuring on the webpage.
    # intended to be used on websites that have dynamic loading. Otherwise, load should be sufficient
    # Interval : The amount of time between checks to see if the web page has changed
    # Period : The number of times that the check must pass before we officially say that the webpage is loaded
    # Period * Interval should equal the longest wait time that you are expecting between elements loading
    def full_load(self, url=None, interval=0.05, period=20, timeout=5):
        if url is not None:
            self.driver.get(url)

        res = False

        i = 0
        p = 0

        start = dt.now()
        end = dt.now()

        while not res:
            temp1 = self.driver.find_elements(By.XPATH, "//*")

            self.driver.implicitly_wait(interval - (start - end))

            temp2 = self.driver.find_elements(By.XPATH, "//*")

            res = compare_page(temp1, temp2)

            end = dt.now()





    # NAVIGATE TO
    # This will either open a url or set the object that the driver is currently manipulating
    # called the "target"
    def navigate_to(self, locator, url=None):
        if url is not None:
            self.full_load(url)

        try:
            WebDriverWait(self.driver, 1).until(locator.ec())

        except exc.TimeoutException as e:
            print("Unable to find " + locator.title + " on this webpage: " + self.driver.current_url)
            raise e
