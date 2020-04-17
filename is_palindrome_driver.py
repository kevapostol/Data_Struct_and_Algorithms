#!/usr/bin/env python3
from is_palindrome import Solution

driver = Solution()

# Should be TRUE
print("input: 9339")
print("output: {}".format(driver.isPalindrome(9339)))

# Should be FALSE
print("input: 12345")
print("output: {}".format(driver.isPalindrome(12345)))

# Should be TRUE
print("input: 1")
print("output: {}".format(driver.isPalindrome(1)))

# Should be FALSE
print("input: -1")
print("output: {}".format(driver.isPalindrome(-1)))
