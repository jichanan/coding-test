class Solution:
    def duplicateZeros(self, arr 
        #: List[int]
        ) -> None:
        """
        Do not return anything, modify arr in-place instead.
        아무것도 반환하지 말고 제자리에서 arr을 수정하시오.
        """
        lth = len(arr)
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
        del arr[lth:]