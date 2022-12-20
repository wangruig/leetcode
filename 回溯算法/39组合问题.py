"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]

示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]
"""

from typing import List

class Solution:

    def combine(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # 采用回溯
        def backtrack(candidates, start, track):
            # 剪枝
            if sum(track) > target:
                return 
            # 终止条件
            if sum(track) == target:
                ans.append(track[:])
                return 
            for i in range(start, len(candidates)):
                track += [candidates[i]]
                backtrack(candidates, i, track)
                track.pop()        
        backtrack(candidates, 0, [])
        return ans

if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    s = Solution()
    ans = s.combine(candidates, target)
    print(f'ans: {ans}')