# 나의 풀이 O(n^2)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
            ans = []
            for i in range(1, len(nums)+1):
                if i not in nums:
                    ans.append(i)
            return ans

# 솔루션 O(n)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
            max_num = len(nums)
            answer = list(set(range(1,max_num + 1)) - set(nums))
            return answer