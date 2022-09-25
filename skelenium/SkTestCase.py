# SK TEST CASE

# This is the main functionality for skelenium. Use the Test Case class to define one test case with an associated suite
# of tests. Use the functions in this class to manipulate the driver

import unittest
import json

from abc import ABC

from skelenium.SkDriver import SkDriver
from skelenium import SkGlobals as Gbs


class TestCase(unittest.TestCase, ABC):

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.account = None
        self.driver = None
        self.config_data = json.load(open("../Unittests/config.json"))
        Gbs.paths = self.config_data["driver_paths"]

    def __del__(self):
        self.driver.quit()

    def setUp(self):
        print("** Test Output **")

    def tearDown(self):
        if self._testMethodDoc is not None:
            print("** Test Code **")
            function_name = self._testMethodName

            f = open(self._testMethodDoc, 'r')
            lines = f.readlines()

            num_space = 0
            record = False
            for line in lines:
                line_space = len(line) - len(line.lstrip())

                if (function_name in line) or ("__init__" in line) and (not record):
                    num_space = line_space
                    record = True
                    print("_" * line_space, end="")
                    print(line)
                    continue

                if (line_space is num_space) and record:
                    print("_")
                    record = False
                    continue

                if record:
                    print("_" * line_space, end="")
                    print(line)

            f.close()

            print("_\n" * 2, end='')
            print("** Locators **")
            print("_")

            self.driver.__print_locators__()


