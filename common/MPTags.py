# MP TAGS
# this contains the code to process the browser decorators for each test
# These tags skip tests if the test is not meant to run on this browser
# It is not built to tag a class
#
# USE SYNTAX:
# from common import MPTags
# @MPTags.skip(drivers=[**list of tags**])
# def test_to_skip():
#    ** Code that might get skipped **

import unittest
import os

# Tags indicating a specific browser
SAFARI = "Safari"
EDGE = "Edge"
CHROME = "Chrome"
FIREFOX = "Firefox"
OPERA = "Opera"
ALL = "All"


# tag a test to skip it
def skip_on_browser(drivers):
    def decoration_skip(test):
        run = True

        try:
            # Make sure that the test is not tagged for this browser
            for driver in drivers:
                # check a tag to see if it is on this browser
                if os.environ["DRIVER"] == driver:
                    run = False

                # if the all tag is present just set it to not run
                if driver == ALL:
                    run = False
        except TypeError:
            print("drivers should be an array of strings defined by the MPTag file. Canceling Test")
            run = False

        # Skip if necessary
        @unittest.skipIf(not run, "This test is not supported on this browser")
        def run_test(self):
            test()

        return run_test
    return decoration_skip
