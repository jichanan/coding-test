class Solution:
    def firstUniqChar(self, s: str) -> int:
        test = list(s)
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in dic:
            if dic[i] == 1:
                return test.index(i)

        return -1