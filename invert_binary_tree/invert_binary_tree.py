'''
Inverts a binary tree
'''
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def invert_tree(root):
    if not root:
        return None
    right = invert_tree(root.right)
    left = invert_tree(root.left)
    root.left = right
    root.right = left
    return root
