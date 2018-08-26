'''
O(2^n)
'''
def powerset(s):
    result = [[]]
    for elem in s:
        result.extend([x + [elem] for x in result])
    return result