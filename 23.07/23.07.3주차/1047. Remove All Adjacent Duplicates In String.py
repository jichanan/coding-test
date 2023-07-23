class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []  

        for char in s:
            if result and char == result[-1]:
                result.pop()
            else:
                result.append(char)

        ans = ''.join(result)

        return ans