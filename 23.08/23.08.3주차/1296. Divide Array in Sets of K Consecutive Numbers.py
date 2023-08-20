# 나의 풀이 (시간초과)
class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        while nums != []:
            m = min(nums)
            t = list(range(m,m+k,1))

            for i in t:
                if i in nums:
                    nums.remove(i)
                else:
                    return False
        return True

# 솔루션
from collections import Counter, defaultdict

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        counter = Counter(nums)
        min_num = min(counter.keys())
        
        while counter:
            for num in range(min_num, min_num + k):
                if counter[num] > 0:
                    counter[num] -= 1
                else:
                    return False
                
            next_num = min([num for num in counter.keys() if counter[num] > 0], default=None)
            if next_num is None:
                break
            min_num = next_num
        
        return True