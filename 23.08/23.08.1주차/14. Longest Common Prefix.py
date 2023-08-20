class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        leng = len(min(strs, key=len))
        tem = set()
        ans = ''

        for i in range(leng):
            for j in range(len(strs)):
                tem.add(strs[j][i])
            if len(tem) == 1:
                str_tem = ''.join(tem)
                ans += str_tem
                tem = set()
            else:
                break

        return ans