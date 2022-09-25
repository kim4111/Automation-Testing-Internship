# MP CUSTOMER SCREEN
# Tests the ways that the user can record customer information on the back-end

from System_Tests.common import MPGlobals as Gbs
from System_Tests.common.MPCommonFunctions import MPCommonFunctions as Cmf
from System_Tests.common import MPTestAccounts as Acs

from System_Tests.screens.MPScreen import MPScreen

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ENTER CUSTOMER SCREEN
# A static function used at the start of each test to make sure that we always start in the same place
def enter_customer_screen():
    if Gbs.MPDriver.current_url == Gbs.portal_base_url:
        Cmf().enter_dashboard_screen(Acs.main_account)
    elif not Gbs.MPDriver.current_url == Gbs.portal_base_url + "/customer":
        Gbs.MPDriver.get(Gbs.portal_base_url+"/customer")

    WebDriverWait(Gbs.MPDriver, 10).until(EC.url_matches(Gbs.portal_base_url + "/customer"))

    return


# @unittest.skip("temp")
# MP CUSTOMER SCREEN
# This class contains of the tests for the Customer Screen
class MPCustomerScreen(MPScreen):
    # TEST ELEMENT VISIBILITY
    # test to make sure that all of the elements on the screen that should be there are there
    # We are testing 9 elements in this test
    def test_element_visibility(self):
        enter_customer_screen()

        passed_test = 0

        # test customer
