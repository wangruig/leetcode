"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]

示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution:

    def sumcombine(self, k, n):

        ans = []
        def backtrack(start, track):
            # 剪枝
            if sum(track) > n:
                return 
            if len(track) == k:
                if sum(track) == n:
                    ans.append(track[:])
                    return 
            # if len(track) == k and sum(track) == n:
            #     ans.append(track[:])
            #     return 
            for i in range(start, 10):
                track +=  [i]
                backtrack(i+1, track)
                track.pop()
        backtrack(1, [])
        return ans

if __name__ == '__main__':
    k = 3
    n = 9
    s = Solution()
    ans = s.sumcombine(k, n)
    print(f'ans: {ans}')