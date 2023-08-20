class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        tem = {}
        ans = []

        for word in list1:
            if word in list2:
                idx = list1.index(word) + list2.index(word)
                tem[word] = idx

        min_value = min(tem.values())

        for i in tem:
            if tem[i] == min_value:
                ans.append(i)

        return ans