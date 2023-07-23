class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        tem = date.split()
        mon = month.index(tem[1]) + 1
        day = tem[0][:-2]


        if len(str(mon)) == 1:
            mon = '0' + str(mon)

        if len(str(day)) == 1:
            day = '0' + str(day)

        ans = f'{tem[2]}-{mon}-{day}'

        return ans