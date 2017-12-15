class Solution():
    def longestPalindrome(self, s):
        n = 0
        substr1 = ''
        substr2 = ''
        longestSubstr = ''
        if len(s) == 1:
            return s
        while n <= len(s) - 1:
            i = 1
            j = 0
            substr1, substr2 = s[n], s[n]
            while n - i >= 0 and n + i < len(s) and s[n - i] == s[n + i] :
                substr1 = s[n-i:n+i+1]
                i += 1
            if n - i < 0:
                substr1 = s[0:n+i]
            elif n + i == len(s):
                substr1 = s[n-i+1:len(s)]

            while n - j >= 0 and n + j + 1 < len(s) and s[n-j] == s[n+j+1]:
                substr2 = s[n-j:n+j+2]
                j += 1
            if n - j < 0:
                substr2 = s[0:n+j+1]
            elif n + j + 1== len(s)-1:
                substr2 = s[n-j+1:len(s)-1]
            if len(substr1) >= len(substr2) and len(substr1) > len(longestSubstr):
                longestSubstr = substr1
            elif len(substr2) >= len(substr1) and len(substr2) > len(longestSubstr):
                longestSubstr = substr2
            n += 1
        return longestSubstr

demo = Solution()
print(demo.longestPalindrome('cccc'))

