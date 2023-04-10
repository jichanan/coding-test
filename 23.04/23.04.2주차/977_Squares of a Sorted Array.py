# 실행시간 초과 (오답)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for num in nums:
            arr += [num ** 2]
        def sort(arr):
            if len(arr) < 2:
                return arr
            else:
                pivot = arr[0]
                less = [i for i in arr[1:] if i <= pivot]
                greater = [i for i in arr[1:] if i > pivot]
                return sort(less) + [pivot] + sort(greater)
        answer = sort(arr)
        return answer

# 솔루션
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in nums: answer.append(i**2)
        answer.sort()
        return answer