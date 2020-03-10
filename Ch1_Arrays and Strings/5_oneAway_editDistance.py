#
# # Solution 1:
# # insertion: when str2 len is 1 less than str1
# # delection: when str2 len is 1 more than str2
# # replace: when str2 len == str1 len
# # if none of the above then return false
# # check if 0 or 1 edits away
#
#
# def editDistance(str1, str2):
#
#     l1 = len(str1)
#     l2 = len(str2)
#
#     # when len of str1 > str2 (insertion case)
#     if(l1-1 == l2 or l1 == l2):
#         ss = str2
#         bs = str1
#
#     # when len of str2 > str1 (removal case)
#     elif(l1+1 == l2):
#         ss = str1
#         bs = str2
#     else:
#         return False
#
#
#     slen = len(ss)
#     blen = len(bs)
#
#     unmatch = 0
#     idx = 0
#
#
#     if(str1[0] != str2[0]):
#         unmatch = unmatch + 1
#
#
#     for i in range(1, slen):
#         try:
#             if(idx != -1):
#                 idx = bs[idx+1:].index(ss[i])
#         except ValueError:
#             # print(bs[idx+1:])
#             # print(ss[i])
#             idx = -1
#             unmatch = unmatch + 1
#
#             if(unmatch > 1):
#                 return False
#
#
#     if (unmatch == 0) and (blen - slen == 1): # insertion and removal case
#         print("Insertion or removal case")
#         return True
#     elif (unmatch == 1) and (l1 == l2):
#         print("Replace case")
#         return True
#     else:
#         return False
#
#


# Solution 2: O(n) time complexity
# insertion: when str2 len is 1 less than str1
# delection: when str2 len is 1 more than str2
# replace: when str2 len == str1 len
# if none of the above then return false

def editDistance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    if (l1-1 == l2): # s1 is greater
        return insertion_removal(s2, s1, l2, l1)

    elif (l1+1 == l2): # s2 is greater
        return insertion_removal(s1, s2, l1, l2)

    elif l1 == l2:
        return replace(s1, s2)

    else:
        return False


def replace(s1, s2):
    edit = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            edit = edit + 1
            if edit > 1:
                return False
    return True


# make sure s2 is the longer string here
def insertion_removal(s1, s2, l1, l2):
    i = 0
    j = 0
    edit = 0

    # l1 < l2
    while i < l1 and j < l2:
        if(s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            edit = edit + 1
            j += 1
            if edit > 1:
                return False
    return True


s1 = "pale"
s2 = "ple"

print(editDistance(s1, s2))
