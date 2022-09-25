# MP ACCESS CONTROL SCREEN
# Tests all of the ways that a user can control employee access through roles

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exc

from System_Tests.common import MPGlobals as Gbs
from System_Tests.common import MPCommonFunctions as Func

from MPScreen import MPScreen
import unittest

# ENTER ACCESS CONTROL
# Go to the access control page no matter where we are
def enter_access_page(url=Gbs.portal_base_url+Gbs.access_control):
    Gbs.MPDriver.get(Gbs.portal_base_url + Gbs.access_control)

    # if we are already in the access control page there is no need to do anything
    if not Gbs.MPDriver.current_url == Gbs.portal_base_url + Gbs.access_control:
        # attempt to go to the dashboard
        Func.MPCommonFunctions().enter_dashboard_screen()

        # if we are in the dashboard attempt to go to the access control
        try:
            WebDriverWait(Gbs.MPDriver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a/i[@class='mp_access_management']")))

            ac_link = Gbs.MPDriver.find_element_by_xpath("//a/i[@class='mp_access_management']")
            ac_link.click()
        except exc.TimeoutException as e:
            print("Attempt to load dashboard Timed out")
            raise e

        # make sure that we make it to access control
        try:
            WebDriverWait(Gbs.MPDriver, 10).until(
                lambda x: Gbs.MPDriver.current_url == Gbs.portal_base_url + Gbs.access_control)
        except exc.TimeoutException as e:
            print("Attempt to load Access Control page Timed out")
            raise e
    return


# MP ACCESS CONTROL SCREEN
# test the elements available on the access control screen
class MPAccessControlScreen(MPScreen):
    @unittest.skip("Under Construction")
    # TEST TOP LINKS
    # make sure that all three links at the top of the access control pages are working correctly
    def test_top_links(self):

        inner_text = [("Roles", Gbs.portal_base_url + Gbs.access_control),
                      ("Privileges", Gbs.portal_base_url + Gbs.access_control_priv),
                      ("Department", Gbs.portal_base_url + Gbs.access_control_dept)]

        # TEST NAV LINKS
        # simple utility function
        # Test all three top nav links on a given page
        # returns the number of times that the tests succeeded
        def nav_links(url=Gbs.portal_base_url + Gbs.access_control):
            # open up the correct page
            enter_access_page(url)

            # get ready to loop
            successes = 0

            # check all three links
            for link in inner_text:
                try:
                    # check for visibility
                    WebDriverWait(Gbs.MPDriver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//a[contains(@id, 'supercategoryLink') and text()='" + link[0] + "']")))
                    link_obj = Gbs.MPDriver.find_element_by_xpath(
                        "//a[contains(@id, 'supercategoryLink') and text()='" + link[0] + "']")
                    successes += 1

                    # check that the link works
                    link_obj.click()
                    WebDriverWait(Gbs.MPDriver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//a[contains(@id, 'supercategoryLink') and text()='" + link[0] + "']")))
                    # make sure that we actually went to the correct web page
                    self.assertTrue(Gbs.MPDriver.current_url == link[1], "The '" + link[0] + "' link at '" + url +
                                    "' lead to " + Gbs.MPDriver.current_url)
                    successes += 1
                except exc.TimeoutException as e:
                    print("The '" + link[0] + "' link on this page is not functioning correctly: " + url)
                    raise e

                # return to the original page
                enter_access_page(url)

            return successes

        # use our utility function to run through each of the links at the top
        successes = nav_links(url=inner_text[0][1]) +\
            nav_links(url=inner_text[1][1]) +\
            nav_links(url=inner_text[2][1])

        self.assertTrue(successes == 18, "There was an uncaught error in the nav links")

    # TEST SEARCH AND SORT
    # Test the search bar and the sort drop down at the top of each page
    @unittest.skip("Under Construction")
    def test_search_and_sort(self):
        urls = [Gbs.portal_base_url + Gbs.access_control,
                Gbs.portal_base_url + Gbs.access_control_priv,
                Gbs.portal_base_url + Gbs.access_control_dept]

        def search_and_sort_page(url):
            return

        successes = search_and_sort_page(urls[0]) +\
            search_and_sort_page(urls[1]) +\
            search_and_sort_page(urls[2])

