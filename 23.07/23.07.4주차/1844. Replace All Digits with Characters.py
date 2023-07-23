class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        ans = ''

        for i in range(len(s)):
            if i % 2 == 1:
                a = s[i-1]
                b = alphabet.index(a)
                tem = b + int(s[i])
                s[i] = alphabet[tem]

        s = ''.join(s)
        return s