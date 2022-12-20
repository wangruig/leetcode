"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出： [[1,1,2], [1,2,1], [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution:

    def permute(self, nums):
        def backtrack(nums, path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            

        if not nums:
            return []
        ans = []
        nums.sort()
        backtrack(nums, [])
        return ans