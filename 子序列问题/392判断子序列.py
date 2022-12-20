"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1： 输入：s = "abc", t = "ahbgdc" 输出：true

示例 2： 输入：s = "axc", t = "ahbgdc" 输出：false

提示：

0 <= s.length <= 100
0 <= t.length <= 10^4
两个字符串都只由小写字符组成。
"""

class Solution:

    def judgesubsequence(self, s: str, t: str) -> bool:
        # dp[i][j] 为以i-1为下标结尾的字符串s是否是以j-1为下标结尾的字符串t的子序列
        # 初始化 dp[i][0] = 0, dp[0][j] = 0
        # 转移 if s[i-1]==t[j-1]: dp[i][j] = dp[i-1][j-1]+1 else: dp[i][j] = dp[i][j-1]

        n = len(s)+1
        m = len(t)+1
        dp = [[0]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] == len(s)


if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgdc'
    so = Solution()
    ans = so.judgesubsequence(s, t)
    print(f'ans: {ans}')