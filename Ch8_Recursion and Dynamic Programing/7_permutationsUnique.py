
import itertools

# A string of length N will cause N-2 calls of the permutations() function. At each call of
# permutations(), the helper() function will produce a list of strings that is N! long.

# Time complexity: O(N!*N^2)

# Space complexity: O(N!*N) because N! no. of strings of length N must be stored.


# Solution 1: Non recursive solution

# Consider the example of 'ab'

# def permutations(target, ch):
#     perm = []
#     l = len(target)
#
#     # first target is [['a']], since the length is 1, perm = [['a'], ['a']]
#     perm.extend([target[:] for i in range(l+1)])
#     i = 0
#
#     # here ch is 'b', first b is inserted at pos 0 then at pos 1
#     for p in perm:
#         p.insert(i, ch)
#         i = i + 1
#
#     # perm = [['b', 'a'], ['a', 'b']]
#     return perm
#
#
# def helper(init, ii):
#     newer = []
#     if ii == 1:
#         return [[init[0][0],li[ii]], [li[ii], init[0][0]]]
#     else:
#         for word in init:
#             newer = newer + permutations(word, li[ii])
#
#     return newer
#
#
#
# str1 = "ab"
# li = [s for s in str1]
#
# # stage = [['a']]
# stage = [[str1[0]]]
#
# # for each character in the string
# for ii in range(1, len(li)):
#     stage = helper(stage, ii)
#
#
# print(stage)
# print(len(stage))
#
# # Just to confirm my answer
# actualAns = [list(x) for x in itertools.permutations(str1)]
# print(sorted(stage) == sorted(actualAns))



# Solution 2: Same logic as above (adding char in all possible positions), but this solution is recursive
# and slightly more concise.

def permutations(str):
    if len(str) <= 0:
        return None
    elif len(str) == 1:
        return [str]
    elif len(str) == 2:
        return [str, str[::-1]]

    else:
        return combine(str[0], permutations(str[1:]))


def combine(char, string_list):
    output_string_list = []

    for string in string_list:
        for i in range(len(string) + 1):
            output_string_list += [string[0:i] + char + string[i:]]

    return output_string_list



str1 = 'abc'
myAns = permutations(str1)
print(myAns)

# Just to confirm my answer
actualAns = [''.join(x) for x in itertools.permutations(str1)]
# print(actualAns)
print(sorted(myAns) == sorted(actualAns))
