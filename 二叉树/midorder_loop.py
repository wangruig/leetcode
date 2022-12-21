"""
"""
from tree_struct import build_tree

class Solution:

    def minorder(self, root):
        """
        递归方法
        1.创建结果列表
        2.进行递归
        """
        def _recursion(node, ans_list):
            """
            递归逻辑
            1.递归参数返回，参数为node和结果列表，返回为结果列表
            2.结束条件，当node为None时返回
            3.递归逻辑：左中右
            """
            if not node:
                return ans_list
            ans_list = _recursion(node.left, ans_list)
            ans_list.append(node.val)
            ans_list = _recursion(node.right, ans_list)
            return ans_list

        ans_list = []
        _recursion(root, ans_list)
        return ans_list
        
if __name__ == '__main__':
    root = build_tree([1, None, 2, None, None, 3])
    s = Solution()
    ans = s.minorder(root)
    print(f'ans: {ans}')