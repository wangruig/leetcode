"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1:

输入：text1 = "abcde", text2 = "ace" 输出：3 解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2: 输入：text1 = "abc", text2 = "abc" 输出：3 解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3: 输入：text1 = "abc", text2 = "def" 输出：0 解释：两个字符串没有公共子序列，返回 0。

提示:

1 <= text1.length <= 1000
1 <= text2.length <= 1000 输入的字符串只含有小写英文字符。
"""

class Solution:
    
    def longestcommonsubsequence(self, text1: str, text2: str) -> int:
        # 动态规划 
        # dp[i][j] 定义为长度[0, i-1]的text1和长度为[0, j-1]的text2的最长公共子序列长度
        # 初始化dp[i][0]和dp[0][j] = 0
        # 转移:
        m = len(text1)+1
        n = len(text2)+1
        dp = [[0]*n for _ in range(m)]
        ans_str = ''
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans_str += text1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1], ans_str


if __name__ == '__main__':
    text1 = 'abc'
    text2 = 'def'
    s = Solution()
    ans, ans_str = s.longestcommonsubsequence(text1, text2)
    print(f'ans: {ans}, ans_str: {ans_str}')