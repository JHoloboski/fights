#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

'''
Solution is O(t1 * t2) as we may need to check the same nodes in t1 as many
times as there are nodes in t2
'''
def isSubtree(t1, t2):
    # if t2 is None, we've traversed that subtree fully, so can return True
    if t2 is None:
        return True
    # however if t2 is not None and t1 is, we've reached a bad traversal, as there's
    # still more to t2. t1's current traversal can't be a subtree, so return False.
    if t1 is None:
        return False

    # if we have both t1 and t2, we can check for their equivalence, or
    # try to find a subtree from another starting point in t1.
    return is_equal(t1, t2) or isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
    
def is_equal(t1, t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.value != t2.value:
        return False
    
    # Getting through our base cases above, we know we have a node that's equal, so
    # we can traverse both subtrees and keep looking for equality until we hit
    # leaf nodes on both sides or we hit values that aren't equal
    return is_equal(t1.left, t2.left) and is_equal(t1.right, t2.right)