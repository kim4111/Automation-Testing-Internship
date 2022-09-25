from collections import defaultdict

from selenium.common.exceptions import NoSuchElementException
from selenium.common import exceptions as Exc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from System_Tests.screens.MPScreen import MPScreen

from time import sleep

from System_Tests.common import MPGlobals
from System_Tests.common import MPLocators as Lcs
from System_Tests.common.MPCommonFunctions import MPCommonFunctions
import unittest


# @unittest.skip("temp")
class MPDashboardScreen(MPScreen):

    def test_inactive_sidebar(self):
        # Can be used on every page except reports. This creates a dictionary with each title and url.
        # I then search the page for the xpath of that title then see if the url associated with the title
        # matches the desired url. In the test I verify that the href+url are correct

        MPCommonFunctions().enter_dashboard_screen()
        passing = 0
        try:
            sidebar = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//ul[@class='list-unstyled components']")))

            sidebar_items = defaultdict(list)
            sidebar_items["Dashboard"] = "https://dev-portal.metispro.com/dashboard"
            sidebar_items["Report"] = "https://dev-portal.metispro.com/reports/dashboard"
            sidebar_items["Catalog"] = "https://dev-portal.metispro.com/catalog-management/supercategory"
            sidebar_items["Inventory"] = "https://dev-portal.metispro.com/stocks/inventory"
            sidebar_items["Employee"] = "https://dev-portal.metispro.com/employee"
            sidebar_items["Customer"] = "https://dev-portal.metispro.com/customer"
            sidebar_items["Access Control"] = "https://dev-portal.metispro.com/access-control"
            sidebar_items["Time Management"] = "https://dev-portal.metispro.com/time-management"
            sidebar_items["Promotion"] = "https://dev-portal.metispro.com/promotion/rule"
            sidebar_items["Coupon"] = "https://dev-portal.metispro.com/coupon"
            sidebar_items["Data Management"] = "https://dev-portal.metispro.com/data-management"
            sidebar_items["Configuration"] = "https://dev-portal.metispro.com/settings/general-information"

            for k, v in sidebar_items.items():

                try:
                    element = MPGlobals.MPDriver.find_element_by_xpath("//li[@title='" + str(k) + "']")
                    try:
                        # Make sure that the text is displayed correctly
                        element = MPGlobals.MPDriver.find_element_by_xpath("//li[@title='" + str(k) + "']//a")
                        if str(k) in element.text:
                            passing += 1
                        else:
                            print("Incorrect Text is Displayed for Sidebar Item:" + element.text)
                            print("Expected Text:" + str(k))

                        # Make sure that the link goes to the correct URL
                        link = element.get_attribute('href')
                        if not link == str(v):
                            print(str(k) + " Leads to Incorrect Link:" + str(link))
                            print("Expected Link:" + str(v))
                        else:
                            passing += 1
                    except NoSuchElementException:
                        print(str(k) + " Link Does Not Exist in the Sidebar")
                except NoSuchElementException:
                    print(str(k) + " Does Not Exist in the Sidebar")
            result = passing == 24


        except:
            result=False
            print("Sidebar Button not Found / Page not Loaded")
        self.assertTrue(result)

    def test_active_sidebar(self):
        # This is only testing whether the sidebar can be toggled. It can be used on every screen including
        # reports except configuration because it does not allow sidebar to be toggled.
        MPCommonFunctions().enter_dashboard_screen()
        try:
            sidebar_collapse = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "mp_ic_menu")))
            sidebar_active = MPGlobals.MPDriver.find_element_by_xpath("//nav[@id='sidebar']")

            if sidebar_active.get_attribute('class') and\
                "active" in sidebar_active.get_attribute('class'):

                result = False
                print("Sidebar is Active Without the Button Being Clicked")
            else:
                sidebar_collapse.click()
                if "active" in sidebar_active.get_attribute('class'):
                    result = True
                else:
                    result= False
                    print("Sidebar Collapse Button Does Not Work")

        except NoSuchElementException:
            result= False
            print("Sidebar Collapse Button Not Found")
        self.assertTrue(result)

    def test_quantic_logo(self):
        # This test can also be used on every screen. The starting part of the quantic logo is always the same.
        MPCommonFunctions().login_function()
        try:
            logo = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//span[starts-with(@class, 'portal__logo')]")))
            logo.click()
            if "{}/dashboard".format(MPGlobals.portal_base_url) in MPGlobals.MPDriver.current_url:
                result= True
            else:
                print("Quantic Logo Does Not Redirect To Dashboard")
                print("It redirects to :" + str(MPGlobals.MPDriver.current_url))
                result=False
        except NoSuchElementException:
            result= False
            print("Quantic Logo Does Not Exist")
        self.assertTrue(result)

    def test_page_header(self):
        # the xpath for each screen with a header is the same, so this test can be reused

        MPCommonFunctions().enter_dashboard_screen()
        try:
            header = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[@class='page__heading']"))
            )
            if "Dashboard" == str(header.text):
                result=True

            else:
                print("Expected Page Header: 'Dashboard' ")
                print("Actual Page Header :" + str(header.text))
                result=False
        except:
            print("Page Header Not Found")
            result = False
        self.assertTrue(result)

    def test_settings(self):
        # xpath for the dropdown stays consistent throughout pages. I did not test the locations aspect of this
        # since I only had access to one location. Also, the "profile" button in dropdown does not appear on
        # settings and reports menu. I do not understand how the logout process worked, so I just verifed
        # that the href to that was correct.
        # In the test I basically look for the element and verify that the text+href are correct
        MPCommonFunctions().enter_dashboard_screen()

        try:
            result = False

            # find the profile image so that it can be clicked later
            dropdown = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located(Lcs.user_icon))
            if dropdown.get_attribute('aria-expanded'):
                print("Dropdown is Visible Without Being Clicked")
                result = False
                self.assertTrue(result)

            # click on the profile image to show the dropdown
            dropdown.click()
            try:
                WebDriverWait(MPGlobals.MPDriver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'col-4') and contains(@class, 'text-right') and contains(@class, 'show')]")))
            except Exc.TimeoutException:
                print("Dropdown is Not Visible After Being Clicked")
                self.assertTrue(False)

            # set up this value for later
            passing = 0

            # test the profile link
            try:
                profile_button = MPGlobals.MPDriver.find_element_by_xpath(
                    "//div[@id='logoutMenuDiv']//div[@class='border_bottom']//a[@class='dropdown-item']")
                if not "https://dev-portal.metispro.com/profile" == profile_button.get_attribute('href'):
                    print("Profile Button Leads to Incorrect Link:" + str(profile_button.get_attribute('href')))
                    print("Expected Link:" + "https://dev-portal.metispro.com/profile")
                    passing += 1
                if not str(profile_button.text) == "Profile":
                    print("Profile Button Displays Incorrect Name:" + str(profile_button.text))
                    passing += 1

            except NoSuchElementException:
                print("Profile Button Does Not Exist In Dropdown Menu")
                result = False
                self.assertTrue(result)

            # Test the logout link
            try:
                # Check the link that shows the modal pop-up
                logout_button = MPGlobals.MPDriver\
                    .find_element_by_css_selector('#logoutMenuDiv > div:nth-child(3) > a:nth-child(1)')
                if str(logout_button.text) != "Logout":
                    print("Logout Button Displays Incorrect Name:" + str(logout_button.text))
                    passing += 1

                # check the link that logs the user out
                logout_button.click()
                modal_logout = WebDriverWait(MPGlobals.MPDriver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "//a[contains(@class,'btn') and contains(@class,'btn-outline-danger') and contains(@class,'d-inline') and contains(@class,'mx-2')]")))
                if not "https://dev-portal.metispro.com/logout" == modal_logout.get_attribute('href'):
                    print("Logout Button Leads to Incorrect Link:" + str(logout_button.get_attribute('href')))
                    print("Expected Link:" + "https://dev-portal.metispro.com/logout")
                    passing += 1

            except NoSuchElementException:
                print("Logout Button Does Not Exist")
                result = False
                self.assertTrue(result)

            # make sure that both of the tests passed
            if passing == 0:
                result = True
            self.assertTrue(result)

        except NoSuchElementException:
            print("Logout / Change Location Dropdown Does Not Exist Or Page Is Not Loaded")
            result = False
            self.assertTrue(result)

    def test_top_monetary_values(self):
        # I could never get the POS and the online system to match data in terms of value, so I just created
        # a skeleton, so that you could input the values in later to check if they match.
        # I was also unable to test credit/coupons. Void/Discount seems to be working fine.
        # Another thing I do not know how to test is the graphs. Like in the pie graph I couldn't test
        # if the pie itself was displayed correctly in terms of the size of each pie based on cost.
        # In this test I basically check to see if the value and label of each report on the page is correct
        # I divided this test into 2 tests to make it easier to read in case of errors
        passing = 0
        result = False
        MPCommonFunctions().enter_dashboard_screen()
        try:
            gross_sale_element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class=' col-xl-3 pt-md-3 col-md-3 pt-xl-0 col-6']//h1")))
            gross_sale_value= 0.00
            gross_sale_string= "$" + str(format(gross_sale_value, '.2f')) + "\nGROSS SALE"
            if gross_sale_string != str(gross_sale_element.text):
                passing += 1
                print("Gross Sale Value Is Incorrect:" + str(gross_sale_element.text))
                print("Expected Gross Sale Value Is:" + gross_sale_string)
        except NoSuchElementException:
            passing += 1
            print("Gross Sale Value Not Found On Page")

        try:
            net_sale_element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='col-md-3 col-xl-3 col-md-3 pt-0 pt-xl-0 col-6']//h1")))
            net_sale_value = 0.00
            net_sale_string = "$" + str(format(net_sale_value, '.2f')) + "\nNET SALE"
            if net_sale_string!= str(net_sale_element.text):
                passing += 1
                print("Net Sale Value Is Incorrect:" + str(net_sale_element.text))
                print("Expected Net Sale Value Is:" + net_sale_string)

        except NoSuchElementException:
            passing += 1
            print("Net Sale Value Not Found On Page")

        try:
            total_order_element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='col-md-3 col-xl-3 col-md-3  pt-3 pt-xl-0 col-6']//h1")))
            total_order_value = 0
            total_order_string = str(total_order_value) + "\nTOTAL ORDERS"
            if total_order_string != str(total_order_element.text):
                passing += 1
                print("Total Orders Value Is Incorrect:" + str(total_order_element.text))
                print("Expected Total Order Value Is:" + total_order_string)

        except NoSuchElementException:
            passing += 1
            print("Total Order Value Not Found On Page")

        try:
            total_guests_element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-3 col-xl-3  pt-3 pt-xl-0 col-6']//h1")))
            total_guests_value = 0
            total_guests_string = str(total_guests_value) + "\nTOTAL GUEST"
            if total_guests_string != str(total_guests_element.text):
                passing += 1
                print("Total Guests Value Is Incorrect:" + str(total_guests_element.text))
                print("Expected Total Guests Value Is:" + total_guests_string)

        except NoSuchElementException:
            passing += 1
            print("Total Guests Value Not Found On Page")
        if passing == 0:
            result = True
        self.assertTrue(result)

    @unittest.skip("Under Construction")
    def test_bottom_monetary_values(self):
        passing = 0
        result = False
        MPCommonFunctions().enter_dashboard_screen()

        # discounts
        try:
            discounts = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@id='discountComp']/..")))
            number_of_discounts = 0
            value_of_discounts = 0.00
            discounts_string = str(number_of_discounts)\
                + " for "\
                + "$"\
                + str(format(value_of_discounts, '.2f'))\
                + "\nDiscounts/Comp"
            if discounts_string != str(discounts.text):
                passing += 1
                print("Discounts Value Is Incorrect:" + str(discounts.text))
                print("Expected Discounts Value Is:" + discounts_string)
        except NoSuchElementException:
            passing += 1
            print("Discounts/Comp Value Does Not Exist")

        # voids
        try:
            voids = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@id='voids']/..")))
            number_of_voids = 0
            value_of_voids = 0.00
            voids_string = str(number_of_voids) + " for " + "$" + str(format(value_of_voids, '.2f')) + "\nVoids"
            if voids_string != str(voids.text):
                passing += 1
                print("Voids Value Is Incorrect:" + str(voids.text))
                print("Expected Voids Value Is:" + voids_string)
        except NoSuchElementException:
            passing += 1
            print("Voids Value Does Not Exist")

        # gross credit
        try:
            gross_credit = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//i[@class='mp_credit-card']/../..//h4")))
            credit_gross_value = 0.00
            credit_string_gross = "Deposit: " + "$" + str(format(credit_gross_value, '.2f'))
            if credit_string_gross != str(gross_credit.text):
                passing += 1
                print("Gross Credit Value Is Incorrect:" + str(gross_credit.text))
                print("Expected Gross Credit Value Is:" + credit_string_gross)

        except NoSuchElementException:
            passing += 1
            print("Gross Credit Value Does Not Exist")

        # net credit
        try:
            net_credit = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//i[@class='mp_credit-card']/../following-sibling::div")))
            credit_net_value = 0.00
            credit_string_net = "$" + str(format(credit_net_value, '.2f')) + "\nNet Sale"
            if credit_string_net != str(net_credit.text):
                passing += 1
                print("Net Credit Value Is Incorrect:" + str(net_credit.text))
                print("Expected Net Credit Value Is:" + credit_string_net)

        except NoSuchElementException:
            passing += 1
            print("Net Credit Value Does Not Exist")

        # gross cash
        try:
            gross_cash = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//i[@class='mp_cash-management']/../..//h4")))
            cash_gross_value = 0.00
            cash_string_gross = "Deposit: " + "$" + str(format(cash_gross_value,'.2f'))
            if cash_string_gross != str(gross_cash.text):
                passing += 1
                print("Gross Cash Value Is Incorrect:" + str(gross_cash.text))
                print("Expected Gross Cash Value Is:" + cash_string_gross)

        except NoSuchElementException:
            passing += 1
            print("Gross Cash Value Does Not Exist")

        # net cash
        try:
            net_cash = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//i[@class='mp_cash-management']/../following-sibling::div")))
            cash_net_value = 0.00
            cash_string_net = "$" + str(format(cash_net_value, '.2f')) + "\nNet Sale"
            if cash_string_net != str(net_cash.text):
                passing += 1
                print("Net Cash Value Is Incorrect:" + str(net_cash.text))
                print("Expected Net Cash Value Is:" + cash_string_net)
        except NoSuchElementException:
            passing += 1
            print("Net Cash Value Does Not Exist")

        # supercategories graph
        try:
            supercat_sale_element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//p[@id='supcatgross']")))
            supercat_sale_value= 0.00
            supercat_sale_string= "$" + str(format(supercat_sale_value, '.2f'))
            if str(supercat_sale_element.text) != supercat_sale_string:
                passing += 1
                print("Supercategory Sales Value Is Incorrect:" + str(supercat_sale_element.text))
                print("Expected Supercategory Sales Value Is:" + supercat_sale_string)

            # Here I make a way to test the expected sales for each category in the graph. Right now
            # this one will fail. Series name has a "x" wherever there is a space, so the k values in the
            # default dict will need to be adjusted if theres a space in the category name.
            categories= defaultdict(list)
            categories["Food"] = "0.00"
            for k, v in categories.items():
                element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//g[@seriesName='"+ str(k) + "']//path")))
                if element.get_attribute('data:value') != v:
                    passing += 1
                    print("Category:" + str(k) + " Has Incorrect Pay Value:" + element.get_attribute('data:value'))
                    print("Expected Pay Value for" + str(k) + "is:" + str(v))
        except NoSuchElementException:
            passing += 1
            print("Supercategory Sales Are Not Listed")

        # I could not input any credit values, so I do not know how that changes the graph/numbers at the top
        # of the "Sales By Pay Type" box
        try:
            pay_type_element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@class='prize_l']")))
            pay_type_value = 0.00
            pay_type_string = "$" + str(format(pay_type_value, '.2f'))
            if str(pay_type_element.text) != pay_type_string:
                passing += 1
                print("Pay Type Value Is Incorrect:" + str(pay_type_element.text))
                print("Expected Pay Type Value Is:" + pay_type_string)

            categories = defaultdict(list)
            categories["Cash"] = "0.00"
            for k, v in categories.items():
                element = WebDriverWait(MPGlobals.MPDriver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//g[@seriesName='" + str(k) + "']//path")))
                if element.get_attribute('val') != v:
                    passing += 1
                    print("Pay Type:" + str(k) + " Has Incorrect Pay Value:" + element.get_attribute('val'))
                    print("Expected Pay Value for" + str(k) + "is:" + str(v))
        except NoSuchElementException:
            passing += 1
            print("Pay Type Sales Is Not Listed")

        if passing == 0:
            result = True
        self.assertTrue(result)

    def test_date_selector(self):
        # There is a date selection bug. I explained it in more detail on the word doc
        passing = 0
        MPCommonFunctions().enter_dashboard_screen()
        try:
            # I don't know why but the page loaded function doesn't always work. Sometimes "b" on line
            # 430 is still not loaded and the test fails. So, I made b have a waiting command as well
            # in order to overcome this.
            sleep(3)
            # I have tried nearly everything and I still can't figure out why this won't work.
            # The "datepicker" in line 435 still fails to be found after the datepicker_test,so
            # I just added a wait.

            datepicker_test = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='daterangepicker']")))
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")

            try:
                b_test = WebDriverWait(MPGlobals.MPDriver, 10).until
                (EC.presence_of_element_located((By.XPATH, "//div[@class='daterangepicker ltr show-calendar opensright']")))
            except NoSuchElementException:
                print("Page is Not Fully Loaded / Date Picker Dropdown Does Not Exist")
            b = MPGlobals.MPDriver.find_element_by_xpath(
                "//div[@class='daterangepicker ltr show-calendar opensright']").is_displayed()

            if b:
                print("Datepicker Displays Itself Without Being Clicked")
                result = False
                self.assertTrue(result)
            datepicker.send_keys("")
            if not(MPGlobals.MPDriver.find_element_by_xpath(
                    "//div[@class='daterangepicker ltr show-calendar opensright']").is_displayed()):
                print("Datepicker Does Not Display Even When Clicked")
                result = False
                self.assertTrue(result)

            apply_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']")
            datepicker.clear()
            datepicker.send_keys("04/05/2021 - 04/08/2021")
            apply_button.click()

            # apply button refreshes the page so I have to find the datepicker again
            sleep(1)
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.click()
            # the datepicker itself does not change the "value" attribute when the dates are changed
            # so I had to look at this one instead
            date_values = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']/..//span")
            if date_values.text != "04/05/2021 - 04/09/2021":
                passing += 1
                print("Unexpected Dates After Clicking Apply:" + date_values.text)
                print("Expected Dates: 04/05/2021 - 04/09/2021 ")

            datepicker.clear()
            datepicker.send_keys("03/05/1996 - 05/08/3000")
            apply_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']")
            apply_button.click()
            sleep(1)
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.click()
            date_values = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']/..//span")
            if date_values.text != "03/05/1996 - 05/09/3000":
                passing += 1
                print("Unexpected Dates After Long Time Frame is Selected:" + date_values.text)
                print("Expected Dates: 03/05/1996 - 05/09/3000 ")

            # Here I test button selection rather than typing in the time frame
            date_1 = MPGlobals.MPDriver.find_element_by_xpath("//div[@class='drp-calendar left']//td[text()='13']")
            date_1.click()
            # calendar refreshes when clicked so I have to find it again
            date_1 = MPGlobals.MPDriver.find_element_by_xpath("//div[@class='drp-calendar left']//td[text()='13']")
            date_1.click()
            apply_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']")
            apply_button.click()
            sleep(1)
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.click()
            date_values = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']/..//span")
            if date_values.text != "03/13/1996 - 03/14/1996":
                passing += 1
                print("Unexpected Dates After Picking Dates Using Buttons:" + date_values.text)
                print("Expected Dates: 03/13/1996 - 03/14/1996")

            # Here I do a test the forward and back buttons
            p = 5
            while p > -1:
                prev_button = MPGlobals.MPDriver.find_element_by_xpath(
                    "//div[@class='drp-calendar left']//th[@class='prev available']")
                prev_button.click()
                p -= 1
            date_1 = MPGlobals.MPDriver.find_element_by_xpath("//div[@class='drp-calendar left']//td[text()='13']")
            date_1.click()
            f=5
            while f > -1:
                forward_button = MPGlobals.MPDriver.find_element_by_xpath(
                    "//div[@class='drp-calendar right']//th[@class='next available']")
                forward_button.click()
                f -= 1
            date_2 = MPGlobals.MPDriver.find_element_by_xpath("//div[@class='drp-calendar right']//td[text()='13']")
            date_2.click()
            apply_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']")
            apply_button.click()
            sleep(1)
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.click()
            date_values = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']/..//span")
            if date_values.text != "09/13/1995 - 04/14/1996":
                passing += 1
                print("Unexpected Dates After Picking Dates Using Forward/Back Buttons:" + date_values.text)
                print("Expected Dates: 09/13/1995 - 04/14/1996")

            # I test the cancel button after typing in the search bar
            cancel_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Cancel']")
            datepicker.clear()
            datepicker.send_keys("09/13/2010 - 08/14/2036")
            cancel_button.click()
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.click()
            date_values = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']/..//span")
            if date_values.text != "09/13/1995 - 04/14/1996":
                passing += 1
                print("Unexpected Dates After Clicking Cancel:" + date_values.text)
                print("Expected Dates: 09/13/1995 - 04/14/1996")

            # I test the cancel button after picking the dates using the buttons
            cancel_button = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Cancel']")
            date_1 = MPGlobals.MPDriver.find_element_by_xpath("//div[@class='drp-calendar left']//td[text()='13']")
            date_1.click()
            date_2 = MPGlobals.MPDriver.find_element_by_xpath("//div[@class='drp-calendar right']//td[text()='13']")
            date_2.click()
            cancel_button.click()
            datepicker = MPGlobals.MPDriver.find_element_by_xpath("//input[@id='daterangepicker']")
            datepicker.click()
            date_values = MPGlobals.MPDriver.find_element_by_xpath("//button[text()='Apply']/..//span")
            if date_values.text != "09/13/1995 - 04/14/1996":
                passing += 1
                print("Unexpected Dates After Clicking Cancel:" + date_values.text)
                print("Expected Dates: 09/13/1995 - 04/14/1996")

        except NoSuchElementException:
            result = False
            print("Date Range Picker Not Found")
            self.assertTrue(result)
