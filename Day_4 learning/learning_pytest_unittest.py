
# Pytest

# one of the most popular testing frameworks is pytest, due to its simplicity, ease of use, and features
# Pytest offers features such as test discovery, fixtures, parameterization, and plugins, which simplify and enhance the testing process.
# What is Unit Testing?
# Unit testing is a software testing technique that focuses on testing individual units of code, usually functions or methods, in isolation.

# Pytest offers several advantages over other testing frameworks in Python, such as unittest and nose
# Simplified syntax
# Automatic test discovery
# Rich plugin ecosystem

# pytest supports all Python versions above 3.7
# pip install pytest

# # math_utlis.py
# def divide(a: int, b: int) -> float:
#     """Return the result of a division operation between two numbers.

#     Args:
#         a (int): The numerator.
#         b (int): The denominator.

#     Returns:
#         float: The result of the division operation.

#     Raises:
#         ZeroDivisionError: If b is zero.
#     """
#     if b == 0:
#         raise ZeroDivisionError("You can't divide by zero!")
#     return a / b

# # test_math_utlis.py
# from src.math_utils import divide


# def test_divide_positive_numbers() -> None:
#     """Test that divide returns the correct result when given two numbers."""
#     assert divide(1, 2) == 0.5


# def test_divide_negative_numbers() -> None:
#     """
#     Test that divide returns the correct result when given a positive and
#     a negative number.
#     """
#     assert divide(5, -2) == -2.5
#     assert divide(-2, 5) == -0.4

# assert statement, which checks that the result of the divide function is equal to the expected result. If an assertion fails, pytest will stop and report the failure.


# to check this in root directory cmd write command pytest
# shows that the test is passed or failed if failed we got an assertion error


# Handling failed tests

# If Pytest reported that the test failed, indicating that the expected result was something else. The failed assert statement is also highlighted in red, and its line indicated. By changing the expected result back to correct one at the defined line, the test will pass again

# Testing for exceptions
# In a divide function, we raise a ZeroDivisionError if the denominator is zero,test to ensure that this exception is raised correctly.

# import pytest

# def test_divide_by_zero() -> None:
#     """Test that divide raises a ZeroDivisionError when the denominator is zero."""
#     with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
#         divide(1, 0)

# fixtures to reuse test data

# to avoid the need for instantiating objects in each test you write, you can create fixtures that can be passed as parameters to the test functions

# we’ve created a fixture called user that returns a new User instance with an ID, name and age. We then passed this fixture as an argument to our test functions, allowing us to reuse the User instance across multiple tests: test_user_creation to test that the User object is created with the correct name and age, and test_greet to test the greet method’s output

# Mock to isolate tests

# Testing interactions can be hard because it involves setting up test databases or APIs, adding test data, and cleaning up after each test. To make testing easier, can use Python’s unittest.mock library. It allows to mimic (“mock”) methods, replacing the real connection with a fake one for testing your function.

# example, what if we have a database with a users table and want to create User objects from that data? We can mock the database connection during testing to return a fake list of users to separate our tests from the database, eliminating the need for a connection and preventing cascading failures: when tests depending on the database fail if it is unavailable.

# pip install sqlalchemy ## needed for accessing sql db in python

# suppose we have a function that connects to a users table and fetches a list of users
# To test this function without connecting to a database, can utilize Python’s built-in unittest.mock.create_autospec function. This allows you to create a mock object that mimics the behavior of SQLAlchemy’s Session


# Unit Testing is the first level of software testing where the smallest testable parts of software are tested.
# Assert Methods in Python Unittest Framework
# assertEqual(a, b) Checks if a is equal to b, similar to the expression a == b.

# .assertTrue(x) Asserts that the boolean value of x is True, equivalent to bool(x) is True.

# .assertIsInstance(a, b) Asserts that a is an instance of class b, similar to the expression isinstance(a, b).

# .assertIsNone(x) Ensures that x is None, similar to the expression x is None.

# .assertFalse(x) Asserts that the boolean value of x is False, similar to bool(x) is False.

# .assertIs(a, b) Verifies if a is identical to b, akin to the expression a is b.

# .assertIn(a, b) Checks if a is a member of b, akin to the expression a in b.

# test fixture: A test fixture is used as a baseline for running tests to ensure that there is a fixed environment in which tests are run so that results are repeatable. Examples :
# creating temporary databases.
# starting a server process.
# test case: A test case is a set of conditions which is used to determine whether a system under test works correctly.
# test suite: Test suite is a collection of testcases that are used to test a software program to show that it has some specified set of behaviours by executing the aggregated tests together.
# test runner: A test runner is a component which set up the execution of tests and provides the outcome to the user.

# import unittest

# def add(a, b):
#     return a + b

# class TestAddFunction(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -2), -3)

#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, -2), -1)
#         self.assertEqual(add(-1, 2), 1)

# if __name__ == '__main__':
#     unittest.main()

# "-v" option is added in the command line while running the tests to obtain more detailed test results(shows the specific output)
