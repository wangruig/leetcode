"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
"""

from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums:
                ans.append(path[:])
                return 
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
        if not nums:
            return []
        ans = []
        backtrack(nums, [])
        return ans

if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    ans = s.permute(nums)
    print(f'ans: {ans}')