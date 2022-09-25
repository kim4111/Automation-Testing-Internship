# MP CONFIGURATION SCREEN
# Tests all of the setting configurations that a user can apply to their account
import selenium.common.exceptions

from System_Tests.screens.MPScreen import MPScreen
from System_Tests.common import MPGlobals as Gbs

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



core_pos_links = {
    "Basic Configuration" : (By.XPATH, "//ul[@class='general-information']/li/a/i[@class='mp_i-configuration']"),
    "General Information" : None,
    "Hardware" : None,
    "Payment"  : None,
    "Printing" : None,
    "Reporting" : None,
    "Service Area" : None,
    "Logging" : None,
}

setup_links = {
    "General Information" : [By.XPATH, "//ul[@id='setup']/li/a[@class='act_lf_nav']", ],
    "Service Area" : None,
    "Tax" : None,
    "User Defined Payment Method" : None,
    "Terminal" : None,
    "GL Accounts" : None,
    "Price List" : None,
    "Predefined Reasons" : None,
    "Discounts" : None,
    "Printer" : None,
    "Predefined Notes" : None,
    "Predefined Gratuity" : None,
    "Gratuity" : None,
    "Course List" : None,
    "Store Hours" : None,
    "Meal Period" : None,
    "Extra Fields" : None,
    "Cash Discount" : None,
    "Predefined Tips" : None,
    "Extra Charge"  : None
}

# MP CONFIGURATION SCREEN
# This class will test all of our settings and ensure that each one does what it is supposed to. A lot of these
# settings require integration with iOS. We still need to look into how to test this.
class MPConfigurationScreen (MPScreen):
    # TEST CORE POS NAVIGATION
    # test to make sure that all of the left side elements appear correctly and are navigating to the correct webpage
    def test_core_pos_navigation(self):
        loc = setup_links["General Information"]
        try:
            config_icon = WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@title='Configuration']")))
            config_icon.click()
            WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable(loc))
        except selenium.common.exceptions.TimeoutException as exc:
            print(exc)

        link = Gbs.MPDriver.find_element(loc[0], loc[1])
        link.click()

        return



