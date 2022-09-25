# TEST SKELENIUM

# This an example of how to use skelenium as well as my testing for the framework

import os

from skelenium.SkAccount import Account
from skelenium import SkDriver as SkDriver
from skelenium import SkLocator
from skelenium import SkTags as St

from skelenium import SkTestCase as Tc
from skelenium import SkCommonFunctions as Skc

# Accounts
main = Account("https://dev-portal.metispro.com/", "pos@qsrdemo21.com", "Quantic21#")

# Locators
username = SkLocator.SkLocator(SkLocator.Conditions.ElementClickable,
                                SkLocator.Identifier.ID,
                                "userName",
                               main.url)
password = SkLocator.SkLocator(SkLocator.Conditions.ElementClickable,
                                SkLocator.Identifier.ID,
                                "password",
                               main.url)
login_button = SkLocator.SkLocator(SkLocator.Conditions.ElementClickable,
                                   SkLocator.Identifier.ID,
                                   "login",
                                   main.url)


# TEST SKELENIUM
# Created: 11/9/2021
# this class provides an example of how to use the framework
class TestSkelenium(Tc.TestCase):
    # The init function should always pretty be exactly this. You can replace
    # the driver with a number of other tags. Note that the "ALL" tag is current not supported
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # prints out your code describing the test
        self._testMethodDoc = os.path.abspath(__file__)
        self.driver = SkDriver.SkDriver(St.CHROME, main)

    # TEST LOGIN BUTTON
    # This tests a login button on the portal
    def test_login_button(self):
        # target username
        self.driver.set_target("Username", username)
        self.driver.load_target()
        self.driver.write_to_target("pos@qsrdemo21.com")

        # target password
        self.driver.set_target("Password", password)
        self.driver.load_target()
        self.driver.write_to_target("Quantic21#")

        # target login button
        self.driver.set_target("Login Button", login_button)
        self.driver.load_target()
        self.driver.click()

        return

    # TEST COMMON LOGIN
    # test to make sure that the common function successfully logs you in
    def test_common_login(self):
        Skc.login(self.driver)

        print(self.driver.driver.current_url)
        if self.driver.driver.current_url != main.url + "dashboard":
            self.assertTrue(False, "The login function did not successfully log us in")
        return

    def test_complicated_loading(self):
        Skc.enter_dashboard(self.driver)
    # TEST
