class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum = 0

        mat_reverse = mat.copy()
        mat_reverse.reverse()
        half = int(len(mat) / 2)

        for i in range(len(mat)):
            sum += mat[i][i]

        for x in range(len(mat_reverse)):
            sum += mat_reverse[x][x]

        if len(mat) % 2 == 1:
            sum -= mat[half][half]
        
        return sum