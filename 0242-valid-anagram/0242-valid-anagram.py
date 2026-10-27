class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            f = [0] * 256
            for letter in s: 
                f[ord(letter)] += 1
            for letter in t:
                f[ord(letter)] -= 1
            return all(count == 0 for count in f)
        return False
