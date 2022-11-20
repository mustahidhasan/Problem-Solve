class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first_half = ord(s[0])
        second_half = ord(s[1])

        if first_half == 40 and second_half == 41:
            return True
        elif first_half == 123 and second_half == 125:
            return True
        elif first_half == 91 and second_half == 93:
            return True
        else:
            return False
