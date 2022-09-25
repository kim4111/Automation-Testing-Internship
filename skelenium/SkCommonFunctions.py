# COMMON FUNCTIONS
# Here is a list of common functions that you can plug a driver into and let it do some of the work for you

from skelenium import SkLocator as Skl
from skelenium import SkGlobals as Gbs


# LOGIN
# login into an account defined by the driver
def login(driver):
    user = driver.account.username
    passw = driver.account.password

    # locators
    username = Skl.SkLocator(Skl.Conditions.ElementClickable,
                             Skl.Identifier.ID,
                             "userName",
                             driver.account.url)
    password = Skl.SkLocator(Skl.Conditions.ElementClickable,
                             Skl.Identifier.ID,
                             "password",
                             driver.account.url)
    login_button = Skl.SkLocator(Skl.Conditions.ElementClickable,
                                 Skl.Identifier.ID,
                                 "login",
                                 driver.account.url)

    loaded = Skl.SkLocator(Skl.Conditions.ElementVisible,
                           Skl.Identifier.ID,
                           "allGrossSale",
                           driver.account.url + Gbs.dash_ext)

    # login
    driver.set_target("login.Username", username)
    driver.load_target()
    driver.write_to_target(user)

    driver.set_target("login.Password", password)
    driver.load_target()
    driver.write_to_target(passw)

    driver.set_target("login.Button", login_button)
    driver.load_target()
    driver.click()

    driver.set_target("Dashboard.GrossSale", loaded)
    driver.load_target()

    print("hit")
    return


def enter_dashboard(driver):
    loaded = Skl.SkLocator(Skl.Conditions.ElementVisible,
                           Skl.Identifier.ID,
                           "allGrossSale",
                           driver.account.url + Gbs.dash_ext)

    driver.get(driver.account.url + Gbs.dash_ext)
    if driver.driver.current_url != driver.account.url + "dashboard":
        login(driver)


def enter_page(driver, extension):

    return
