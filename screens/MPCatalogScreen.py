import selenium.common.exceptions as Ecs
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from System_Tests.common.MPCommonFunctions import MPCommonFunctions
from System_Tests.common import MPLocators as Lcs
from System_Tests.screens.MPScreen import MPScreen

from System_Tests.common import MPGlobals


# MP CATALOG SCREEN
class MPCatalogScreen(MPScreen):

    def enter_catalog_screen(self):
        MPCommonFunctions().enter_dashboard_screen()

        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("Info: Loading gif never appeared")

        element = MPGlobals.MPDriver.find_element_by_class_name("mp_catalog-of-colors")
        element.click()

    def test_click_catalog_tabs(self):
        self.enter_catalog_screen()
        passing = 0
        element = MPGlobals.MPDriver.find_element(Lcs.super_category[0], Lcs.super_category[1])
        element.click()
        header = MPGlobals.MPDriver.find_element_by_class_name("page__heading").text
        if "Super Categories" in header:
            passing += 1
        element = MPGlobals.MPDriver.find_element(Lcs.category[0], Lcs.category[1])
        element.click()
        header = MPGlobals.MPDriver.find_element_by_class_name("page__heading").text
        if "Categories" in header:
            passing += 1
        element = MPGlobals.MPDriver.find_element(Lcs.items[0], Lcs.items[1])
        element.click()
        header = MPGlobals.MPDriver.find_element_by_class_name("page__heading").text
        if "Items" in header:
            passing += 1
        element = MPGlobals.MPDriver.find_element(Lcs.modifiers[0], Lcs.modifiers[1])
        element.click()
        header = MPGlobals.MPDriver.find_element_by_class_name("page__heading").text
        if "Modifier Groups" in header:
            passing += 1
        element = MPGlobals.MPDriver.find_element(Lcs.modifiers[0], Lcs.modifiers[1])
        element.click()
        header = MPGlobals.MPDriver.find_element_by_class_name("page__heading").text
        if "Modifier" in header:
            passing += 1

        if passing == 5:
            return True
        return False

    def test_modifier_group_search(self):
        self.enter_catalog_screen()
        element = MPGlobals.MPDriver.find_element_by_id("modifierLink")
        element.click()
        element = MPGlobals.MPDriver.find_element_by_id("search")
        element.send_keys("nacho")
        searchresults = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "Nacho Toppings" in searchresults and "Nacho Meat" in searchresults:
            element.clear()
            return True
        return False

    def test_items_search(self):
        self.enter_catalog_screen()
        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable(Lcs.items))
        click = MPGlobals.MPDriver.find_element_by_id("groupLink")
        click.click()
        search = MPGlobals.MPDriver.find_element_by_id("itemName")
        search.send_keys("sparkling")
        searchresults = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "Sparkling Lemonade" in searchresults and "Sparkling Waters" in searchresults:
            return True
        return False

    def test_items_tax_class(self):
        self.enter_catalog_screen()
        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable(Lcs.items))
        click = MPGlobals.MPDriver.find_element(Lcs.items[0], Lcs.items[1])
        click.click()
        MPGlobals.MPDriver.find_element_by_name("taxClass")
        passing = 0

        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("Warning: May not be able to find the super category dropdown")

        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_visible_text('no tax')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "SPICY CHICKEN SOUP" in bodyText:
            passing += 1

        try:
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("Warning: May not be able to find the super category dropdown")

        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_visible_text('Default Tax')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "Snapple" in bodyText:
            passing += 1

        try:
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("Warning: May not be able to find the super category dropdown")

        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_visible_text('tax')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "Elote Corn in a Cup " in bodyText:
            passing += 1
        if passing == 3:
            return True
        return False

    # once Super Categories page is more fleshed out
    def test_super_categories_tax_class(self):
        self.enter_catalog_screen()
        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable(Lcs.super_category))
        click = MPGlobals.MPDriver.find_element(Lcs.super_category[0], Lcs.super_category[1])
        click.click()
        MPGlobals.MPDriver.find_element_by_id("taxClass")
        passing = 0
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_value('252FC5F3-B356-4525-AEAE-4B7D59B8F575')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if " " in bodyText: # check search
            passing += 1
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_value('27A4F81C-93D5-423E-8393-095EAC843340')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "" in bodyText: # check search
            passing += 1
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_value('5703BF42-DED6-441D-AD8F-573C823F05E1')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if " " in bodyText: # check search
            passing += 1
        if passing == 3:
            return True
        return False

    # TEST CATEGORIES TAX CLASS
    # Makes sure that the filter by tax class is working correctly
    def test_categories_tax_class(self):
        self.enter_catalog_screen()

        # function to check what super category a category has
        def check_tax_class(web_obj, tax_class):
            # enter the object
            web_obj.click()


        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable(Lcs.category))
        click = MPGlobals.MPDriver.find_element(Lcs.category[0], Lcs.category[1])
        click.click()
        MPGlobals.MPDriver.find_element_by_name("taxClass")
        passing = 0
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_visible_text('no tax')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if " " in bodyText:  # check search
            passing += 1
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_visible_text('Default Tax')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if "" in bodyText:  # check search
            passing += 1
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "taxClass"))
        search.select_by_visible_text('tax')
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text
        if " " in bodyText:  # check search
            passing += 1
        if passing == 3:
            return True
        return False

    # TEST CATEGORIES SUPER CATEGORIES
    # the the super categories dropdown on the categories page
    def test_categories_super_categories(self):
        # Get ready to test
        passing = 0

        # CHECK SUPER CATEGORY
        # Make sure that a given category contains the correct
        # super category
        def check_super_category(web_obj, sup_cat):
            # open this category
            web_obj.click()

            # find the super category
            super_category = WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.visibility_of_element_located((By.ID, "supCat"))).getFirstSelectedOption()

            # double check the category
            if super_category == sup_cat:

                # return to the categories page
                WebDriverWait(MPGlobals.MPDriver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "cancel_btn_set mr-3")))\
                    .click()

                # make sure that the categories page loads
                try:
                    WebDriverWait(MPGlobals.MPDriver, 2).until(
                        EC.presence_of_element_located(Lcs.category))
                    WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
                    WebDriverWait(MPGlobals.MPDriver, 2).until(
                        lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
                except Ecs.TimeoutException:
                    print("INFO: Loading icon did not appear")

                return True

            # if this category does not have the correct super category

            # return to the categories page
            WebDriverWait(MPGlobals.MPDriver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cancel_btn_set mr-3"))) \
                .click()

            # make sure that the categories page loads
            try:
                WebDriverWait(MPGlobals.MPDriver, 2).until(
                    EC.presence_of_element_located(Lcs.category))
                WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
                WebDriverWait(MPGlobals.MPDriver, 2).until(
                    lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
            except Ecs.TimeoutException:
                print("INFO: Loading icon did not appear")

            return False

        self.enter_catalog_screen()

        # make sure that the page has loaded
        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("INFO: Loading icon did not appear")

        # Find the link to go to the categories page and click it
        click = MPGlobals.MPDriver.find_element(Lcs.category[0], Lcs.category[1])
        click.click()

        # Make sure that the page loads
        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("INFO: Loading icon did not appear")

        # Find the correct super category in the dropdown
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "supCat"))
        search.select_by_visible_text("Food")

        # Make sure that the web page loaded
        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("INFO: Loading icon did not appear")

        # check that the categories loaded correctly
        first_result = MPGlobals.MPDriver.find_element_by_xpath(
            "//div[contains(@class,'di_block') and contains(@class,'cat__name')]/a/span")

        print(first_result.text)

        if check_super_category(first_result, "Food"):  # check search
            passing += 1

        # find another super category
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "supCat"))
        search.select_by_visible_text("Gift Card")
        bodyText = MPGlobals.MPDriver.find_elements_by_xpath('')
        if "" in bodyText:  # check search
            passing += 1

        # Make sure that the results loaded
        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("INFO: Loading icon did not appear")

        # Find and test the last super category
        search = Select(MPGlobals.MPDriver.find_element(By.ID, "supCat"))
        search.select_by_visible_text("Retail")
        bodyText = MPGlobals.MPDriver.find_element_by_tag_name('body').text

        if " " in bodyText:  # check search
            passing += 1
        if passing == 3:
            return True
        return False

    def test_super_categories_search(self):
        self.enter_catalog_screen()
        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable(Lcs.super_category))
        click = MPGlobals.MPDriver.find_element(Lcs.super_category[0], Lcs.super_category[1])
        click.click()
        search = MPGlobals.MPDriver.find_element_by_id("search")
        search.send_keys("")
        searchresults = MPGlobals.MPDriver.find_element_by_tag_name('body').text

        if " " in searchresults and " " in searchresults:
            return True
        return False

    # TEST CATEGORIES SEARCH
    # test the search bar in the categories section of the catalogue
    def test_categories_search(self):
        # get ready to test
        self.enter_catalog_screen()

        # Make sure that the page has loaded
        element = WebDriverWait(MPGlobals.MPDriver, 10).until(
            EC.element_to_be_clickable(Lcs.category))
        # If the page has loaded go to the category page
        click = MPGlobals.MPDriver.find_element(Lcs.category[0], Lcs.category[1])
        click.click()

        # Find the search bar and send a search to it
        search = MPGlobals.MPDriver.find_element_by_id("search")
        search.send_keys("sides")

        # Wait for it to load
        try:
            WebDriverWait(MPGlobals.MPDriver, 0.5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            WebDriverWait(MPGlobals.MPDriver, 2).until(
                lambda e: not EC.element_to_be_clickable((By.CLASS_NAME, "loading"))(MPGlobals.MPDriver))
        except Ecs.TimeoutException:
            print("Info: Loading icon did not appear or did not disappear in 2 seconds")

        # Get results
        search_results = MPGlobals.MPDriver.find_elements_by_xpath(
            "//div[@class='di_block cat__name']/a[@class='']")

        # test results
        it = 0
        for result in search_results:
            it += 1
            if not result.text == "":
                self.assertTrue("sides" in result.text.lower(),
                                "In the list of categories, when we searched for sides we got "
                                + result.text
                                + " as a result")
        print("Tested " + str(it) + " results")

    

