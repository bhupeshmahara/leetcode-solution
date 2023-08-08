# time O(n)
# space O(n)

class Solution(object):
    def isPalindrome(self, x):
        return False if x < 0 else x == int(str(x)[::-1])

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]: return True
        return False

# using python reverse function

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        l = x.copy()
        l.reverse()
        if x == l: return True
        else: return False
