from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as Ecs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from System_Tests.common import MPGlobals
from System_Tests.common import MPTestAccounts as Acs


class MPCommonFunctions:

    # LOGIN FUNCTION
    # if we haven't already logged into the account we use this function to log in
    def login_function(self, account=Acs.main_account):
        try:
            MPGlobals.MPDriver.get(account.url)
            login = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.element_to_be_clickable((By.ID, "login")))
            email = MPGlobals.MPDriver.find_element_by_id("userName")
            password = MPGlobals.MPDriver.find_element_by_id("password")
            email.send_keys(account.username)
            password.send_keys(account.password)

            login.click()

        except Exception as e:
            print("Login Failed/ Page Not Loaded")
            raise e

    def select_date_picker(self):
        try:
            WebDriverWait(MPGlobals.MPDriver, 10).until(By.XPATH, '//input[@id=daterangepicker]')
            datepicker = MPGlobals.MPDriver.find_element(By.XPATH, '//input[@id=daterangepicker]')

            datepicker.click()


        except Exception as e:
            print("Date Picker Failed")
            raise e


    # ENTER DASHBOARD SCREEN
    def enter_dashboard_screen(self, account=Acs.main_account):
        # If we are not already logged in make sure to do that
        if MPGlobals.MPDriver.current_url == account.url:
            self.login_function()
        # If we are not already in the dashboard screen, go there
        if not MPGlobals.MPDriver.current_url == account.url + "/dashboard":
            MPGlobals.MPDriver.get(account.url + "/dashboard")

        # Make sure that we have reached the dashboard
        try:
            WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "mp_catalog-of-colors")))

            WebDriverWait(MPGlobals.MPDriver, 2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.UnexpectedAlertPresentException:
            print("There was a weird alert")
        except Ecs.TimeoutException:
            print("Info: loading did not show")

    # DATE SET
    def dateset(self, a, b):
        # This function doesn't seem to have too much use. It simplified my date testing,but it also
        # can be used to match order values/reports for different date ranges. The formatting of inputting
        # dates is annoying so I just made the function to simplify that a tad.
        if MPGlobals.MPDriver.current_url != "https://dev-portal.metispro.com/dashboard":
            MPGlobals.MPDriver.get("https://dev-portal.metispro.com/dashboard")

        try:
            # For some reason I couldn't send input into datepicker1. I think it has something
            # to do with waiting until detected possibly?

            datepicker_test= WebDriverWait(MPGlobals.MPDriver, 10).until
            (EC.presence_of_element_located((By.XPATH, "//input[@id='daterangepicker']")))

            datepicker= MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.clear()
            datepicker.send_keys(a+ " - " + b)
            apply_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']")
            apply_button.click()
        except NoSuchElementException:
            print("Date Range Picker Not Found")

    # IS PAGE LOADED
    def is_page_loaded(self):
        # Mp-cash is one of the last things on the page and visibility should also ensure that
        # I can see it but this doesn't verify if the page is loaded sometimes
        page = WebDriverWait(MPGlobals.MPDriver, 10).until
        (EC.visibility_of_element_located((By.XPATH, "//i[@class='mp_cash-management']")))
