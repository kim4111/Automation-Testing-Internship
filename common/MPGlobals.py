# This is a set of "static" global variables. You should not edit them
# dynamically at all. They should stay the exact same for the entire
# duration of the run-time. Unfortunately the only native ways to do this
# in python are really clunky, so I can't force write perms.

# Set-up / General

class DriverType:
    firefox = "Firefox"
    chrome = "Chrome"
    edge = "Edge"


# The base domain to add extensions to
portal_base_url = "https://dev-portal.metispro.com"
# Contains our main instance of the driver
MPDriver = None
CurrentDriver = None

# URL Extensions
dashboard = "/dashboard"
access_control = "/access-control"
access_control_priv = "/access-control/privilege"
access_control_dept = "/access-control/department"
report = "/reports/dashboard"

# stub
