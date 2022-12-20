"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入： A: [1,2,3,2,1] B: [3,2,1,4,7] 输出：3 解释： 长度最长的公共子数组是 [3, 2, 1] 。

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
from typing import List

class Solution:

    def findlengthofarray(self, A: List[int], B: List[int]) -> int:
        # 动态规划
        # dp[i][j] 表示A[j],B[i]的最长公共子数组
        # 初始化dp[0][0] = 0
        # 转移: 当A[j-1] == B[i-1]时, dp[i][j] = dp[i-1][j-1]+1

        m = len(A)+1
        n = len(B)+1
        dp = [[0]*m for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(1, m):
                if B[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                ans = max(ans, dp[i][j])
        return ans

if __name__ == '__main__':
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    s = Solution()
    ans = s.findlengthofarray(A, B)
    print(f'ans: {ans}')
    
