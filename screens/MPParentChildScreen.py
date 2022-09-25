# MP PARENT CHILD SCREEN
# We need to make sure that the parent child relationship will work for our clients
# For now all of the tests in this list are temporary. We will need to adapt them to work with future clients
# # # DO NOT RUN THESE TESTS UNLESS SPECIFICALLY ASKED TO # # #

import selenium.common.exceptions as exc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from MPScreen import MPScreen

from System_Tests.common import MPGlobals as Gbs, MPMenu as Mu
from System_Tests.common import MPTestAccounts as Acs
from System_Tests.common.MPCommonFunctions import MPCommonFunctions as Cf
import System_Tests.common.MPLocators as Loc

import unittest


@unittest.skip("Under Construction")
class MPParentChildScreen(MPScreen):

    @classmethod
    def setUpClass(cls):
        # I am using this to log into a none default test location
        Cf().login_function(account=Acs.parent_child_account)

        try:
            WebDriverWait(Gbs.MPDriver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "mp_catalog-of-colors")))

        except exc.TimeoutException:
            cls.skipTest(cls, "Skipped Tests Because Log-in Failed")

    @classmethod
    def tearDownClass(cls):
        Cf().login_function()

    # @unittest.skip("Not Finished")
    def test_master_dashboard(self):
        try:
            Cf().enter_dashboard_screen(url="https://myquantic.com")
            WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable(Loc.user_icon))
        except exc.TimeoutException as e:
            if not Gbs.MPDriver.current_url == "https://myquantic.com/dashboard":
                print("Failed to enter dashboard screen")
            raise e

        icon = Gbs.MPDriver.find_element_by_class_name("mp_ic_user")
        icon.click()

    def test_master_create_destroy_menu(self):
        super_categories = ["HQDT", "HQNT"]
        categories = ["default tax", "no tax"]

        # create menu

        # Add two super categories
        # for sc in categories:
        Mu.add_super_category("Hyperion QAT - no tax", "no tax")

        # Add two categories for each super category
        # for c in categories:
        Mu.add_category("HQ - no tax", "Hyperion QAT - no tax", "no tax")

        # Add two items for each category
        for i in range(3):
            Mu.add_item("HQ - " + str(i), "1", "HQ - no tax", categories[0])


        # verify menu in children

        # remove menu
        # for sc in categories:
        for c in range(3):
            Mu.rem_item("HQ - " + c, "HQ - no tax")
        Mu.rem_category("HQ - " + c, "Hyperion QAT - no tax")
        Mu.rem_super_category("Hyperion QAT - " + "no tax")

        # verify removed menu
        return


