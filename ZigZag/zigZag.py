class Solution():
    def convert(self, s, numRows):
        str = []
        s1 = ''
        if numRows == 1:
            return s
        else:
            for i in range(0, numRows):
                str.append([])
            for i in range(0, len(s)):
                numStr = i %(numRows * 2 - 2)
                if numStr < numRows:
                    str[numStr] += s[i]
                else:
                    str[numRows * 2 - 2 - numStr] += s[i]
            for i in range(0,numRows):
                for j in range(0, len(str[i])):
                    s1 += str[i][j]
                # print(str[i])
        return s1

demo = Solution()
print(demo.convert('abcde', 4))

