class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        start_city = []
        arrive_city = []

        for path in paths:
            start_city.append(path[0])
            arrive_city.append(path[1])

        start_city = set(start_city)
        arrive_city = set(arrive_city)

        ans = arrive_city - start_city
        ans = list(ans)
        ans = ans[0]
        return ans