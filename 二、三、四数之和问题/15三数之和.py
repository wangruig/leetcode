"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    """
    算法流程：
    1.对数据进行排序
    2.对数据进行剪枝：包括num[0]>0，num[i-1]和num[i]相同
    3.
    """
    def threesum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            # nums[0] > 0时，结束
            if nums[0] > 0:
                break
            # 过滤掉i和i-1相同的数
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # 第二个数下标
            j = i+1
            # 第三个数下标
            k = len(nums)-1
            while j < k:
                # 如果三个数相加和为0:返回下标
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    # 如果第二个数下标小于第三个数且过滤掉第二个数重复项
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    # 如果第二个数下标小于第三个数下标切过滤掉第三个数重复项
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                # 小于0，第二个数下标++1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                # 大于0，第三个数下标--1
                else:
                    k -= 1
        return ans
                    
     

if __name__ == '__main__':
    nums = [1, 0, -1, 2, -1, -4]
    s = Solution()
    ans = s.threesum(nums)
    print(f'ans: {ans}')