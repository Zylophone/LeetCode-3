class Solution():
    def longestPalindrome(self, s):
        if len(s) == 1 or s == s[::-1]:
            return s
        else:
            maxlen = 1
            start = 0
            for x in range(1, len(s)+1):
                if x - maxlen > 1 and s[x-maxlen-2:x] == s[x-maxlen-2:x][::-1]:
                    start = x - maxlen - 2
                    maxlen += 2
                    continue
                if x - maxlen > 0 and s[x-maxlen-1:x] == s[x-maxlen-1:x][::-1]:
                    start = x - maxlen - 1
                    maxlen += 1

        return s[start:(start+maxlen)]

demo = Solution()
print(demo.longestPalindrome('yu111u'))






