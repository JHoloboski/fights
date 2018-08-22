'''
Really simple solution. O(1) comparison.
'''
def containsDuplicates(a):        
    return len(set(a)) != len(a)