# 시간복잡도 n^2 (실행시간초과)
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        ans = []
        for i in range(len(arr)):
            i += 1
            ans += [max(arr[i:], default=-1)]
        return ans

# 솔루션 
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        answer = [0] * len(arr)
        answer[-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            answer[i] = max([answer[i+1], arr[i+1]])
            
        return answer
