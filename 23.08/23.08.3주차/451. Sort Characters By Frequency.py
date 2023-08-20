class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        tem = {}
        ans = ""

        for i in s:
            if i not in tem:
                tem[i] = 1
            else:
                tem[i] += 1

        while tem != {}:
            max_key = max(tem, key=tem.get)
            ans += max_key * tem[max_key]
            tem.pop(max_key)

            
        return ans