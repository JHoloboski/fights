#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
'''
O(v)
'''
def hasPathWithGivenSum(t, s):
    if not t:
        return False
    
    s -= t.value
    if t.right and t.left:
        return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right, s)
    elif t.right:
        return hasPathWithGivenSum(t.right, s)
    elif t.left:
        return hasPathWithGivenSum(t.left, s)
    
    return s == 0
    