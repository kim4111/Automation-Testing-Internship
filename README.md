# Automation-Systems-Internship

Quantic Portal (also known as Project Hyperion) is Quantic's backend system for our clients to access their business data and manage their system.

The purpose of these automated tests is the ensure the quality of the builds we create for production.

The tests should be updated as features evolve, and a changelog for each test should be included in some capacity. For example, if the developers rewrite a feature to act differently, the test function should include a comment that the test was rewritten on (this date) with (these changes to the feature).

Example: 
```
'''
06/04/2021: Rewrote to accomodate for multiple modifiers instead of one.
'''
```

## Setup

#### System Tests
The setup for this project is that each screen is located in the `screens` directory. Each file that contains tests for the screen should use the following format: `MP{Name Of Screen}Screen.py`.

The `MPCommonFunctions.py` file is to create functions that can be used on multiple screens. The `MPGlobals.py` file is for variables that we might use throughout the tests, such as the base url for the portal.

In your run configuration for the unittests, please add the pattern `MP*Screen.py`.

Finally, remember to install the necessary dependencies for selenium and requests. You may need to install a driver, such as `geckodriver`, for certain browsers.

#### Unit Tests
Unit tests for Hyperion testing will be created using our own framework for selenium that is made to match the needs of our system, Skelenium (working title).

The first thing that you will need to do is set up a config.json file. That file should follow the format:
```
{
  "driver_paths": {
    "firefox" : "",
    "edge" : "",
    "chrome" : "",
    "safari" : "",
    "opera" : ""
  }
}
```
Then you can create a file with your tests. For more about using Skelenium visit our documentation in the docs folder

In PyCharm, when your test has been written you can simply right click the test and select the run option to automatically create a configuration. If you would like to know more about configuring a setup you can take a look at our testing configurations doc, config.md.

## Compatibility
This system is compatible with:

| Priority | Browser |
|----------|---------|
| 1        | Firefox |
| 2        | Chrome  |
| 3        | Safari  |
| 4        | Edge    |
| 5        | Opera   |

## Contact

Please contact [Stephen Sharp](mailto:ssharp@metispro.com) or [Arnav Kaushik](mailto:akaushik@metispro.com) for any questions regarding this project. Be sure to add tickets in the [MetisCollab project](https://collab.metispro.com/project/view/63/) for any tasks you need help with.
