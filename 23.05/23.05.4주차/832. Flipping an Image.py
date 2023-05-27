class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in image:
            i.reverse()
            for x in range(len(i)):
                if i[x] == 0:
                    i[x] = 1
                else:
                    i[x] = 0
        return image