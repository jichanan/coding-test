class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        len_1 = len(word1)
        len_2 = len(word2)

        min_len = min(len_1, len_2)

        for i in range(min_len):
            ans.append(word1[i])
            ans.append(word2[i])

        if len_1 > len_2:
            ans.extend(word1[min_len:])
        else:
            ans.extend(word2[min_len:])

        ans = ''.join(ans)

        return ans