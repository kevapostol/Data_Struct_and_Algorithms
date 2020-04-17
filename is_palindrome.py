#!/usr/bin/env python3


class Solution:
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        # Edge case: if number is neg, return False
        if x <= 0:
            return False

        # int to string conversion
        str_x = str(x)
        str_size = len(str_x)
        right = str_size - 1

        # Palindrome checker
        # O(n)
        for i in range(str_size // 2):
            left = i
            if (str_x[left] != str_x[right]):
                return False
            right -= 1

        return True
