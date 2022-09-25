import unittest
from abc import ABC


class MPScreen(unittest.TestCase, ABC):

    def __init__(self, *args, **kwargs):
        super(MPScreen, self).__init__(*args, **kwargs)

    #! OLD !#
    # # Required setup
    # def setUp(self):
    #     MPGlobals.MPDriver = webdriver.Firefox(executable_path=r'/Users/Stephen/Documents/geckodriver/geckodriver.exe')
    #
    # # Close down when test is done
    # def tearDown(self):
    #     MPGlobals.MPDriver.close()

