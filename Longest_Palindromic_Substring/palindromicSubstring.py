import time
class Solution():
    def longestpalindrome(self, s):
        longestpalindrome = ''
        substring = ''
        if len(s) == 1:
            return s
        for x in range(0,len(s) - 1):
            for n in range(1, len(s) - x + 1):
                substring = s[x:x+n]
                if substring == substring[::-1] and len(substring) >= len(longestpalindrome):
                    longestpalindrome = substring

        return longestpalindrome

timeStart = time.time()
demo = Solution()
# demo.longestpalindrome('1001')
print(demo.longestpalindrome('bbbb'))
print(time.time() - timeStart)