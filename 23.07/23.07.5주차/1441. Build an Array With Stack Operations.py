class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans = []
        test = []

        tem = list(range(1,n+1))

        for i in tem:
            test.append(i)
            ans.append('Push')
            if test[-1] not in target:
                ans.append('Pop')
                test.pop()
            elif test == target:
                break
        
        return ans