"""
列表构建树
"""

class Tree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def show_node(self, layer=0):
        return f'val: {self.val}\n' \
               f'{" " * 4 * (layer + 1)}' \
               f'left: {self.left.show_node(layer + 1) if self.left is not None else None}\n' \
               f'{" " * 4 * (layer + 1)}' \
               f'right: {self.right.show_node(layer + 1) if self.right is not None else None}'

    def __str__(self, layer=0):
        return self.show_node(layer)


def build_tree(vals):
    """
    创建树
    1.生成node
    2.如果左节点存在，则2*i+1
    3.如果右节点存在，则2*i+2
    """
    node_list = [Tree(val) if val else None for val in vals]
    for index, node in enumerate(node_list):
        if not node:
            continue 
        if (2 * index + 1) < len(node_list):
            node.left = node_list[2 * index + 1]
        if (2 * index + 2) < len(node_list):
            node.right = node_list[2 * index + 2]
    return node_list[0] 



if __name__ == '__main__':
    vals = [1, None, 2, 3]
    root = build_tree(vals)
    print(root)
