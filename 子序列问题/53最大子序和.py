"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例: 输入: [-2,1,-3,4,-1,2,1,-5,4] 输出: 6 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

"""

from typing import List



class Solution:

    def maxsubarray(self, nums):
        """
        采用动态规划，dp[i]代表以下标i结尾的nums中的子序列最大和
        """
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
        return max(dp)


class Solutio:

    def maxsubarray(self, nums: List[int]) -> int:
        # dp[i] 为nums[0, i]中以i结尾的连续子数组的最大和
        # 初始化 dp[0] = max(0, nums[0])
        # 转移 若nums[i] >= 0: dp[i] = dp[i-1]+nums[i]; 否则 dp[i] = 0
        
        n = len(nums)
        if not n:
            return 0
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
        return max(dp)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    ans = s.maxsubarray(nums)
    print(f'ans: {ans}')


