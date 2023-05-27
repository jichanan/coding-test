class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        init = [1]
        test = [1,1]
        ans = []
        if numRows == 1:
            ans = [[1]]

        for x in range(numRows-1):
            for i in range(len(init)-1):
                tem = init[i] + init[i+1]
                test.insert(1, tem)
            init = test
            ans += [test]
            test = [1,1]
        if numRows != 1:
            ans.insert(0,[1])
        return ans