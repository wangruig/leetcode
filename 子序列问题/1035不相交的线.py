"""
我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。

现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。

以这种方法绘制线条，并返回我们可以绘制的最大连线数。

输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/uncrossed-lines
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:

    def uncrossedlines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)+1
        n = len(nums2)+1
        dp = [[0]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    s = Solution()
    ans = s.uncrossedlines(nums1, nums2)
    print(f'ans: {ans}')