"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明： 所有数字（包括目标数）都是正整数。 解集不能包含重复的组合。 

示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 所求解集为: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]

示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 所求解集为: [   [1,2,2],   [5] ]
"""

class Solution:

    def combain(self, candidates, target):
        # 回溯
        def backtrack(candidates, start, track):
            # 终止条件
            if sum(track) == target:
                ans.append(track[:])
                return
            for i in range(start, len(candidates)):
                # 剪枝
                if sum(track) + candidates[i] > target:
                    return 
                if i > start and candidates[i] == candidates[i-1]:
                    continue 
                track += [candidates[i]]
                backtrack(candidates, i+1, track)
                track.pop()
        if not len(candidates):
            return []
        ans = []
        # 必须进行排序，避免重复
        candidates.sort()
        backtrack(candidates, 0, [])
        return ans


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    ans = s.combain(candidates, target)
    print(f'ans: {ans}')
            
    