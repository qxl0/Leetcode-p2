class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = [ch.lower() for ch in s if ch.isalnum()]
        n = len(str)
        for i in range(n):
            if str[i] != str[n-1-i]:
                return False
        return True