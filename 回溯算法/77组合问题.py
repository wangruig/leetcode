"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]
"""
from typing import List

class Solution:

    def combine(self, n:int, k:int) -> List[List[int]]:
        ans = []

        def backtrack(n, start, track):
            if len(track) == k:
                ans.append(track[:])
                return 
            for i in range(start, n):
                track = track+[i]
                backtrack(n, i+1, track)
                track.pop()
        backtrack(n+1, 1, [])
        return ans
if __name__ == '__main__':
    n = 4
    k = 2
    s = Solution()
    ans = s.combine(n, k)
    print(f'ans: {ans}')