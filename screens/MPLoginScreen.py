import selenium.common.exceptions as exc

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from System_Tests.screens.MPScreen import MPScreen

from time import sleep

from System_Tests.common import MPGlobals

import unittest

# LOAD_LOGIN_SCREEN
# A small function to define a common operation in this set of tests
def load_login_screen():
    try:
        # attempt to open the webpage. I'll just use the username object to see if it has loaded.
        MPGlobals.MPDriver.get(MPGlobals.portal_base_url)
        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable((By.ID, "userName")))
    except exc.TimeoutException as e:
        # throw this exception if email bar is not found within 10 seconds
        # This could be because the item simply does not exist on the page
        print("Element not Found/Page not Loaded")
        raise e

# @unittest.skip("temp")
class MPLoginScreen(MPScreen):

    # TEST_LOGO
    # Make sure that the logo on the login screen is present,
    # visible and clickable
    def test_logo(self):
        # At end of test, assert this to be true
        result = False

        # Start of test
        try:
            load_login_screen()

            # since we know it exists, select the logo
            logo = MPGlobals.MPDriver.find_element_by_class_name("navbar-brand")

            # Get the url of the link attached to the logo
            link = logo.get_attribute('href')
            print('Expected: https://getquantic.com')
            print('Actual: ' + str(link))
            # Set results of the test in the result object
            if (MPGlobals.portal_base_url + "/index.html") in link:
                result = True
            else:
                print("Logo does not redirect to 'getquantic.com'")
                result = False

        # just some simple redundancy
        except exc.NoSuchElementException as e:
            print("Quantic Logo Not Found")
            result = False

        # Check the test for completion
        self.assertTrue(result)

    # TEST_EMAIL
    # A simple test to ensure that the e-mail/username bar exists
    def test_email(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start test
        try:
            load_login_screen()

            # Select the email bar and fill it with the email "Hello"
            email = MPGlobals.MPDriver.find_element_by_id("userName")
            email.send_keys("hello")
            # Assign a result to the result variable
            if "hello" == email.get_attribute("value"):
                email.clear()
                result = True
            else:
                email.clear()
                result = False

        # Simple Redundancy
        except exc.NoSuchElementException:
            print("Email Bar Does Not Exist")
            result = False

        # Test the result variable to pass/fail the test
        self.assertTrue(result)

    # TEST_PASSWORD
    # A simple test to ensure that the password bar exists
    def test_password(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start Test
        try:
            load_login_screen()

            # Select the password bar and fill it with "Hello"
            password = MPGlobals.MPDriver.find_element_by_id("password")
            password.send_keys("hello")
            # Assign a result to the result variable
            if "hello" == password.get_attribute("value"):
                password.clear()
                result = True
            else:
                password.clear()
                result = False

        # simple redundancy
        except exc.NoSuchElementException:
            print("Password Bar Does Not Exist")
            result = False

        # check if we pass/fail test
        self.assertTrue(result)

    # TEST_TERMS_AND_CONDITIONS
    # This is meant to test that the link to the terms and
    # conditions section works properly
    def test_terms_and_conditions(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start Test
        try:
            load_login_screen()

            # Find/Open the link to the terms and conditions
            element = MPGlobals.MPDriver.find_element_by_xpath("//a[@data-target = '#tncModal']")
            element.click()
            # Get the heading
            body_text = MPGlobals.MPDriver.find_element_by_class_name('report_heading').text
            # Check to make sure that the heading is correct
            if "Terms and Conditions" in body_text:
                close_button = MPGlobals.MPDriver.find_element_by_class_name("close")
                close_button.click()
                result = True
            else:
                print("Terms and Conditions Link Does Not Work")
                result = False

        # redundancy
        except exc.NoSuchElementException:
            print("Terms and Conditions Button Does Not Exist")
            result = False

        # Check to see if the test passed or failed
        self.assertTrue(result)

    # TEST_LANGUAGE_BUTTON
    # test the ability to select a language on the login screen
    # ** UNSTABLE **
    @unittest.skip("Unstable Test - Language button has not been set up")
    def test_language_button(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start Test
        try:
            load_login_screen()

            # Find the language option
            MPGlobals.MPDriver.find_element_by_name("lang")
            # Variable to store # of passing tests
            passing = 0

            element = Select(MPGlobals.MPDriver.find_element(*MPLoginScreenLocators.LANGUAGE_BUTTON))
            element.select_by_value('zh')
            body_text = MPGlobals.MPDriver.find_element_by_tag_name('body').text
            if "以更智能的方式控制您的业务" in body_text:  # need the chinese translation
                passing += 1
            element = Select(MPGlobals.MPDriver.find_element(*MPLoginScreenLocators.LANGUAGE_BUTTON))
            element.select_by_value('en')
            body_text = MPGlobals.MPDriver.find_element_by_tag_name('body').text
            if "Control your business the smarter way" in body_text:
                passing += 1
            element = Select(MPGlobals.MPDriver.find_element(*MPLoginScreenLocators.LANGUAGE_BUTTON))
            element.select_by_value('es')
            body_text = MPGlobals.MPDriver.find_element_by_tag_name('body').text
            if "Controle su negocio de la manera más inteligente" in body_text:  # need the spanish translation
                passing += 1
            if passing == 3:
                result = True
            else:
                result = False

        # Redundancy
        except exc.NoSuchElementException:
            print("Language Button Does Not Exist")
            result = False

        # Check if we pass/fail this test
        self.assertTrue(result)

    # TEST_FORGOT_PASSWORD
    # Test the forgot password link to make sure that it takes the user to the right webpage
    def test_forgot_password(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start Test
        try:
            load_login_screen()

            # Find the forgot item link and click on it
            element = MPGlobals.MPDriver.find_element_by_xpath("//a[@data-target = '.bd-example-modal-lg']")
            element.click()
            # copy the text of the label that appears into a new variable
            body_text = WebDriverWait(MPGlobals.MPDriver, 10).until(EC.visibility_of_element_located(
                (By.ID, "myLargeModalLabel"))).text
            # Check to see if the correct text is present in the header
            if "Forgot Password" in body_text:
                # Check the close button to make sure that it closes the Modal Label
                close_button = MPGlobals.MPDriver.find_element_by_class_name("close_BTN")
                try:
                    close_button.click()
                    close_button.click()
                    close_button.click()
                except:
                    pass
                sleep(1)
                result = True
            else:
                print("Forget Password Link Does Not Work")
                result = False

        # Redundancy
        except exc.NoSuchElementException:
            print("Forget Password Link Does Not Exist")
            result = False

        # Check to see if we pass/fail this test
        self.assertTrue(result)

    # TEST_LOGIN_BUTTON
    # Test whether or not the login button is working correctly
    # This should reject bad username/password combos and pass good combos
    # UNSTABLE
    def test_login_button(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start Test
        try:
            load_login_screen()

            # Find the login button, and the username and password fields
            login = MPGlobals.MPDriver.find_element_by_id("login")
            email = MPGlobals.MPDriver.find_element_by_id("userName")
            password = MPGlobals.MPDriver.find_element_by_id("password")

            # Input dummy username / password
            email.send_keys("hello")
            password.send_keys("goodbye")
            login.click()


            # Make sure that you can't login with this username/password combo
            try:
                WebDriverWait(MPGlobals.MPDriver, 10).until(
                    EC.visibility_of_element_located((By.ID, "loginErrMsg")))
                # Test whether or not the correct error message shows up
                self.assertTrue("Wrong User name or password"
                                in MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text)
            except exc.TimeoutException:
                # Error if the URL leads to the dashboard
                self.assertFalse("{}/dashboard".format(MPGlobals.portal_base_url) in MPGlobals.MPDriver.current_url)
                raise exc.TimeoutException

            # Enter new credentials. Valid username/ invalid password
            email.clear()
            password.clear()
            email.send_keys("pos@qsrdemo21.com")
            password.send_keys("hi")
            login.click()

            # Make sure that you can't login with this username/password combo
            try:
                WebDriverWait(
                    MPGlobals.MPDriver, 10).until(lambda a: "Wrong password"
                                                            in MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text)
                # Tests the text in the error message
                reference = MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text
                self.assertTrue("Wrong password"
                                in MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text)
            except exc.TimeoutException:
                # Error if the URL leads to the dashboard
                self.assertFalse("{}/dashboard".format(MPGlobals.portal_base_url) in MPGlobals.MPDriver.current_url)
                raise exc.TimeoutException

            # Replace the old invalid credentials with valid credentials
            email.clear()
            password.clear()
            email.send_keys("pos@qsrdemo21.com")
            password.send_keys("Quantic21#")
            login.click()

            try:
                WebDriverWait(MPGlobals.MPDriver, 10).until(
                    lambda x: "{}/dashboard".format(MPGlobals.portal_base_url) in MPGlobals.MPDriver.current_url)
                result = True
            except exc.TimeoutException:
                self.assertFalse("Wrong User name or password"
                                 in MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text)
                raise exc.TimeoutException

        # OLD
        #     if "{}/dashboard".format(MPGlobals.portal_base_url) in MPGlobals.MPDriver.current_url:
        #         print("Wrong Username and Password Lets You Login")
        #         result = False
        #     else:
        #         # If it doesn't let you log in make sure that the correct error appears
        #         try:
        #             error = MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text
        #             if "Wrong User name or password" in error:
        #                 # If the correct error appears then input a new set of keys
        #                 # This time e-mail correct, but password wrong
        #                 email.clear()
        #                 password.clear()
        #                 email.send_keys("pos@qsrdemo21.com")
        #                 password.send_keys("hi")
        #                 login.click()
        #
        #                 # Make sure that they can't login with the wrong password
        #                 if "{}/dashboard".format(MPGlobals.portal_base_url) in MPGlobals.MPDriver.current_url:
        #                     print("Wrong Password Lets You Login")
        #                     result = False
        #                 else:
        #                     try:
        #                         # Check error to make sure it shows up correctly
        #                         errortxt = MPGlobals.MPDriver.find_element_by_id("loginErrMsg").text
        #                         if "Wrong password" in errortxt:
        #                             # If error text is correct then try a valid username/ password
        #                             email.clear()
        #                             password.clear()
        #                             email.send_keys("pos@qsrdemo21.com")
        #                             password.send_keys("Quantic21#")
        #                             login.click()
        #
        #                             MPGlobals.MPDriver.implicity_wait(2)
        #                             # Make sure that it lets us through with valid credentials
        #                             if "{}/dashboard".format(MPGlobals.portal_base_url)
        #                                                   in MPGlobals.MPDriver.current_url:
        #                                 result = True
        #                             # If it doesn't let us through fail the test
        #                             else:
        #                                 print("Correct Username and Password Does Not Lead to Dashboard")
        #                                 result = False
        #                         else:
        #                             print("Incorrect Password Message is Incorrect")
        #                             result = False
        #                     except exc.NoSuchElementException:
        #                         result = False
        #             else:
        #                 print("Incorrect Username and Password Message Is Not Correct")
        #                 result = False
        #         except exc.NoSuchElementException:
        #             print("Wrong Username and Password Error Does Not Pop Up")
        #             result = False
        except exc.NoSuchElementException:
            print("Login Button Does Not Exist")
            result = False

    # TEST_SHOW_PASSWORD
    # Test whether or not the user's input will be visible when they press the show password button for
    # the password field
    def test_show_password(self):
        # Holds the value that we will assert against to check whether the test passed
        result = False

        # Start Test
        try:
            load_login_screen()

            password = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.ID, "password")))
            password.send_keys("dummy")

            # Find the view password button and click it
            show_password = MPGlobals.MPDriver.find_element_by_class_name("mp_visibility_off")
            show_password.click()

            # make sure that the visibility is turned on
            try:
                # This will cause an intentional exception if visibility is still off
                show_password_now = WebDriverWait(MPGlobals.MPDriver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mp_visibility")))

                # Input a password into the password field and show the password again
                password = MPGlobals.MPDriver.find_element_by_id("password")
                password.send_keys("hello")
                show_password.click()

                # Turn the visibility on and off again to make sure that it is working
                try:
                    show_pass = MPGlobals.MPDriver.find_element_by_class_name("mp_visibility_off")
                    show_password.click()
                    try:
                        show = MPGlobals.MPDriver.find_element_by_class_name("mp_visibility")

                        # We haven't found any issues. Complete test
                        result = True

                    except exc.NoSuchElementException:
                        print("Hide Password Does Not Work")
                        result = False
                except exc.NoSuchElementException:
                    print("Show Password Does Not Work If Password Is Typed In")
                    result = False
            except exc.NoSuchElementException:
                print("Show Password Does Not Work If No Password Is Typed In")
                result = False
        except exc.NoSuchElementException:
            print("no")
            result = False

        # Check to see if pass/fail test
        self.assertTrue(result)


class MPLoginScreenLocators(object):
    LANGUAGE_BUTTON = (By.ID, "lang")
