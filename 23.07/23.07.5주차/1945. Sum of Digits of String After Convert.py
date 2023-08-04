class Solution:
    def getLucky(self, s: str, k: int) -> int:
        test = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,'h':8,'i':9,'j':1,
        'k':2,'l':3,'m':4,'n':5,'o':6,'p':7,'q':8,'r':9,'s':10,'t':2,
        'u':3,'v':4,'w':5,'x':6,'y':7,'z':8}

        tem = []

        for i in s:
            tem.append(test[i])

        for x in range(k):
            ans = str(sum(tem))
            tem = [int(num) for num in ans]
        ans = int(ans)
        return ans