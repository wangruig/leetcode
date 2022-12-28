"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    """
    流程
    1.构建一个最小堆
    2.遍历arr，维护一个最小堆
    当arr[i] < hp[0]时，进行维护，堆顶pop，将arr[i]push进堆
    """
    def findtopmink(self, arr, k):
        import heapq
        if k == 0:
            return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans





if __name__ == '__main__':
    arr = [3, 2, 1, 0, 1]
    k = 3
    s = Solution()
    ans = s.findtopmink(arr, k)
    print(f'ans: {ans}')