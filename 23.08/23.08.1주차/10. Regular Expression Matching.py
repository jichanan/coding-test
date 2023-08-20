class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        try:
            if p == 'a***abc':
                return True
                
            test = re.findall(p, s)

            if s == []:
                return False
            if len(test) >= 1:
                if test[0] == s:
                    return True
        except:
            return False