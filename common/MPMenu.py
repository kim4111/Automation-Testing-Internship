# MP Menu
# This is a file containing functions commonly used to construct and destruct a menu

import selenium.common.exceptions as exc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from common import MPGlobals as Gbs

# open a page of the menu
def enter_menu_page(extension):
    try:
        Gbs.MPDriver.get("https://myquantic.com/catalog-management/" + extension)
        WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "show_up_to_select")))
    except exc.UnexpectedAlertPresentException as e:
        print(e.msg)
        print("There is an alert that should be here")
        Gbs.MPDriver.get("https://myquantic.com/catalog-management/" + extension)
        WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "show_up_to_select")))
    except exc.TimeoutException as e:
        if not Gbs.MPDriver.current_url == ("https://myquantic.com/catalog-management/" + extension):
            print("Failed to enter dashboard screen")
        raise e

    show = Select(Gbs.MPDriver.find_element_by_class_name("show_up_to_select"))
    show.select_by_value("1000")

    try:
        WebDriverWait(Gbs.MPDriver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException as e:
        if not Gbs.MPDriver.current_url == ("https://myquantic.com/catalog-management/" + extension):
            print("Failed to enter dashboard screen")
        raise e


# functions to create a menu without using the class
def add_super_category(name, tax_class):
    enter_menu_page("supercategory")
    name_field = Gbs.MPDriver.find_element_by_id("search")
    name_field.send_keys(name)

    tc_field = Select(Gbs.MPDriver.find_element_by_id("taxClass"))
    tc_field.select_by_visible_text(tax_class)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    save = Gbs.MPDriver.find_element_by_id("saveSupCat")
    save.click()


def add_category(name, super_category, tax_class):
    enter_menu_page("categories")
    name_field = Gbs.MPDriver.find_element_by_id("search")
    name_field.send_keys(name)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    sc_field = Select(Gbs.MPDriver.find_element_by_id("supCat"))
    sc_field.select_by_visible_text(super_category)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    tc_field = Select(Gbs.MPDriver.find_element_by_id("taxClass"))
    tc_field.select_by_visible_text(tax_class)

    save = Gbs.MPDriver.find_element_by_id("saveCat")
    save.click()


def add_item(name, sale_price, category, tax_class):
    enter_menu_page("items")
    name_field = Gbs.MPDriver.find_element_by_id("itemName")
    name_field.send_keys(name)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    price_field = Gbs.MPDriver.find_element_by_id("price")
    price_field.send_keys(sale_price)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    tc_field = Select(Gbs.MPDriver.find_element_by_id("taxClass"))
    tc_field.select_by_visible_text(tax_class)

    try:
        WebDriverWait(Gbs.MPDriver, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    cat_field = Select(Gbs.MPDriver.find_element_by_id("category"))
    cat_field.select_by_visible_text(category)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    save = Gbs.MPDriver.find_element_by_id("saveItem")
    save.click()


def add_modifier_group(name, tax_class):
    enter_menu_page("modifier-group")
    name_field = Gbs.MPDriver.find_element_by_id("search")
    name_field.send_keys(name)

    tc_field = Select(Gbs.MPDriver.find_element_by_id("taxClass"))
    tc_field.select_by_visible_text(tax_class)

    save = Gbs.MPDriver.find_element_by_id("saveSupCat")
    save.click()


def add_modifier(name, tax_class):
    enter_menu_page("modifier")
    name_field = Gbs.MPDriver.find_element_by_id("search")
    name_field.send_keys(name)

    tc_field = Select(Gbs.MPDriver.find_element_by_id("taxClass"))
    tc_field.select_by_visible_text(tax_class)

    save = Gbs.MPDriver.find_element_by_id("saveSupCat")
    save.click()


# functions to break down the menu
def rem_super_category(name):
    enter_menu_page("supercategory")

    name_link = Gbs.MPDriver.find_element_by_xpath("//a[@class='link-black']/span[text()='" + name + "']")
    name_link.click()

    WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "delete__pro")))
    delete = Gbs.MPDriver.find_element_by_class_name("delete__pro")
    delete.click()

    alert = WebDriverWait(Gbs.MPDriver, 10).until(EC.alert_is_present())
    alert.accept()


# functions to break down the menu
def rem_category(name, super_category):
    enter_menu_page("categories")

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    sc_field = Select(Gbs.MPDriver.find_element_by_id("supCat"))
    sc_field.select_by_visible_text(super_category)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    name_link = Gbs.MPDriver.find_element_by_xpath(
        "//div[contains(@class, 'di_block') and contains(@class, 'cat__name')]/a/span")
    name_link.click()

    # WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "delete__pro")))
    delete = Gbs.MPDriver.find_element_by_class_name("delete__pro")
    delete.click()

    alert = WebDriverWait(Gbs.MPDriver, 10).until(EC.alert_is_present())
    alert.accept()


# functions to break down the menu
def rem_item(name, category):
    enter_menu_page("items")

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    cat_field = Select(Gbs.MPDriver.find_element_by_id("category"))
    cat_field.select_by_visible_text(category)

    try:
        WebDriverWait(Gbs.MPDriver, 0.1).until(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
        WebDriverWait(Gbs.MPDriver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    except exc.TimeoutException:
        print("Timed out")

    name_link = Gbs.MPDriver.find_element_by_xpath(
        "//div[contains(@class, 'di_block') and contains(@class, 'cat__name')]/a/span")
    name_link.click()

    # WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "delete__pro")))
    delete = Gbs.MPDriver.find_element_by_class_name("delete__pro")
    delete.click()

    alert = WebDriverWait(Gbs.MPDriver, 10).until(EC.alert_is_present())
    alert.accept()

def rem_modifier_group(name):
    enter_menu_page("modifier-group")

    name_link = Gbs.MPDriver.find_element_by_xpath("//a[@class='link-black']/span[text()='" + name + "']")
    name_link.click()

    WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "delete__pro")))
    delete = Gbs.MPDriver.find_element_by_class_name("delete__pro")
    delete.click()

    alert = WebDriverWait(Gbs.MPDriver, 10).until(EC.alert_is_present())
    alert.accept()


def rem_modifier(name):
    enter_menu_page("modifier")

    name_link = Gbs.MPDriver.find_element_by_xpath("//a[@class='link-black']/span[text()='" + name + "']")
    name_link.click()

    WebDriverWait(Gbs.MPDriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "delete__pro")))
    delete = Gbs.MPDriver.find_element_by_class_name("delete__pro")
    delete.click()

    alert = WebDriverWait(Gbs.MPDriver, 10).until(EC.alert_is_present())
    alert.accept()
