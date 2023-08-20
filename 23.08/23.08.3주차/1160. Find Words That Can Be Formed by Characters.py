class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
  
        count=0
        for val in words:
            flag=True
            for j in val:
                if val.count(j)>chars.count(j):
                    flag=False
                    break
            if flag:
                count+=len(val)

        return(count)