
# Power Set: Write a method to return all subsets of a set.


# Simple method of finding the power set
# from itertools import combinations
#
# def powerSet(s):
#     ps = []
#     for i in range(0, len(set)+1):
#         ps = ps + list(combinations(['a', 'b', 'c'], i))
#
#     return ps
#
#
# normal method without itertools
# def powerSet(s):
#     ps = []
#
#     for i in range(len(s)):
#         for li in ps:
#             if s[i] not in li:
#                 ps.append(li + [s[i]])
#         ps.append([s[i]])
#
#     return ps


# Recursive method
ps = []

def powerSet(s, ele):
    for li in ps:
        if ele not in li:
            ps.append(li + [ele])
    ps.append([ele])

    if len(s) == 0:
        ps.append([])

    else:
        ele = s.pop(0)
        powerSet(s, ele)

    return ps




set = ["a", "b", "c"]
ele = set.pop(0)
print(powerSet(set, ele))
