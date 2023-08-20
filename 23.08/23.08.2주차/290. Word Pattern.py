class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        zipped = list(zip(pattern, words))
        return len(set(zipped)) == len(set(pattern)) == len(set(words))