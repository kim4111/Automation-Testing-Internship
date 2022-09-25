# A list of all of the locators needed to run the dev portal

from selenium.webdriver.common.by import By


# NAVIGATION

# profile icon on top-right
user_icon = (By.CLASS_NAME, "mp_ic_user")
profile_btn = (By.XPATH, "//a[contains(@class, 'ic_top_bar') and contains(@class, 'showLogoutMenuBtn']")


# ACCESS CONTROL SCREEN


# CATALOG SCREEN

# catalog navigation links
super_category = (By.ID, "supercategoryLink")
category = (By.ID, "categoryLink")
items = (By.ID, "groupLink")
modifiers = (By.ID, "modifierLink")
# Modifier groups and Modifiers have the same id

# clickable link for one of the available catalog items
menu_item = (By.CLASS_NAME, "link-black")


# CONFIGURATION SCREEN


# COUPON SCREEN


# CUSTOMER SCREEN

# Links, Search and Create
customer_link = (By.ID, "supercategoryLink")
customer_group_link = (By.ID, "categoryLink")


# CUSTOMER SCREEN


# DASHBOARD SCREEN


# DATA MANAGEMENT SCREEN


# EMPLOYEE SCREEN


# INVENTORY SCREEN


# LOGIN SCREEN


# PROMOTION SCREEN


# REPORT SCREEN


# TIME MANAGEMENT SCREEN


# TRANSFER SALE SCREEN
