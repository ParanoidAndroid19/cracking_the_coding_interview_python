
# Solution 1:
# To check if s2 ('erbottlewat') is the rotation of s1 ('waterbottle'):
# pos = s1.index(s2[0])
# rot = s1[pos:] + s2[:pos]
# if rot == s2 then return True

# what if there are repeated chars in the str? Then first count no. of occurances of s2[0] in s1,
# if more than 1 then make a list of all indices at which it occures. Do the rest of the procedure for
# all the indices.

# def strRotation(s1, s2):
#
#     # only valid for strRotation and not for isSubstring
#     if len(s1) != len(s2):
#         return False
#
#     indices = []
#
#     for i, c in enumerate(s1):
#         if c == s2[0]:
#             indices.append(i)
#
#     if len(indices) == 0:
#         return False
#
#     for pos in indices:
#         # isSubstring
#         # sub = s1[pos:pos+len(s2)]
#         # if sub == s2:
#         #     print("s2 is a substring of s1")
#         #     return True
#
#         # str rotation
#         rot = s1[pos:] + s1[:pos]
#         if rot == s2:
#             return True
#
#     return False


# solution 2: A different and much easier approach
# eg: killbillkillbill

def isSubstring(string, sub):
    # if sub not in string, find returns -1
    return string.find(sub) != -1


def strRotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return isSubstring(s1 + s1, s2)
    return False


s1 = "killbill"
s2 = "illkillb"

# cases:
# s1 = "waterbottle", s2 = "erbottlewat" --> True
# s1 = "killbill", s2 = "illkillb" --> True
# s1 = "foo", s2 = "bar" --> False
# s1 = "foo", s2 = "foofoo" --> False

# checks if s2 is rotation of s1
print(strRotation(s1, s2))
