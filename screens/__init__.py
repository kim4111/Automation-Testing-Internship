# # __init__.py
# __init__ is a file that runs before everything else by default. I have this file
# set up two functions for the unittest driver to run before and after all of the tests.

from System_Tests.common import MPGlobals
from System_Tests.common.MPCommonFunctions import MPCommonFunctions
from selenium import webdriver
from selenium.webdriver.chrome import service as Cs
from selenium.webdriver.firefox import service as Fs
from selenium.webdriver.safari import service as Ss
from selenium.webdriver.edge import service as Es
# from selenium.webdriver.opera import service as O_s

import unittest
import os


# Start up script
def start_test_run(self):
    # This set-up will select a driver based on the user-defined environment variables set up in each configuration
    # If no driver is included in the environment variables, it will just set up as a firefox driver
    try:
        if os.environ["DRIVER"] == "Chrome":
            cs=Cs.Service(os.environ["DRIVER_PATH"])
            MPGlobals.MPDriver = webdriver.Chrome(service=cs)
            MPCommonFunctions().login_function()
            return

        if os.environ["DRIVER"].lower() == "edge":
            es=Es.Service(os.environ["DRIVER_PATH"])
            MPGlobals.MPDriver = webdriver.Edge(service=es)
            MPCommonFunctions().login_function()
            return

        if os.environ["DRIVER"].lower() == "firefox":
            fs=Fs.Service(os.environ["DRIVER_PATH"])
            MPGlobals.MPDriver = webdriver.Firefox(service=fs)
            MPCommonFunctions().login_function()
            return

        # if os.environ["DRIVER"].lower() == "opera":
        #     o_s=O_s.service(os.environ["DRIVER_PATH"])
        #     MPGlobals.MPDriver = webdriver.Opera(service=o_s)
        #     MPCommonFunctions().login_function()
        #     return

        if os.environ["DRIVER"].lower() == "safari":
            ss=Ss.Service(os.environ["DRIVER_PATH"])
            MPGlobals.MPDriver = webdriver.Safari(service=ss)
            MPCommonFunctions().login_function()
            return

        # If the environment variable doesn't exist or is wrong just use Firefox
        raise Exception("Your DRIVER environment variable is spelled incorrectly")
    except KeyError:
        raise Exception("Your DRIVER or DRIVER_PATH environment variables do not exist")

# Shut Down Script
def stop_test_run(self):
    MPGlobals.MPDriver.quit()


# Make sure unittest knows that the startup script exists
setattr(unittest.TestResult, 'startTestRun', start_test_run)
# Make sure unittest knows that the shutdown script exists
setattr(unittest.TestResult, 'stopTestRun', stop_test_run)