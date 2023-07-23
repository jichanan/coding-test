class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        tem = ''

        for word in words:
            tem += word
            if tem == s:
                return True
                break
        return False