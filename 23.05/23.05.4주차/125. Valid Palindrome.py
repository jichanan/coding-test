class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        test = re.findall('[a-zA-Z0-9]', s)
        test2 = test.copy()
        test2.reverse()
        test = [i.lower() for i in test]
        test2 = [i.lower() for i in test2]
        if test == test2:
            return True
        else:
            return False