import unittest
from tests.home.login_tests import LoginTests
from tests.getfuel.create_SO_tests import RequestFuelTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RequestFuelTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)