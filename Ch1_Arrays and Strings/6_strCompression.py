
# aabcccccaaa --> a2blc5a3

# Solution 1:
# Firstly, to record the repeated chars I will use a bit vector ([0]*n) where index value will be the
# ord (ASCII) of A-Z and a-z. In the same loop if the next letter is different than current letter
# (st[i] != st[i+1]), I will append the required letters and its repetitions in order, after that
# make recorded repetitions for that char 0. Come out of loop and join the list. Compare the len of original
# and compressed string, if len of compressed str is not smaller then return original str
# otherwise return compressed str. complexity is O(n)
#
#
# def strCompression(st):
#
#     char_set = [0]*123
#     res = []
#
#     for i in range(len(st)):
#         idx = ord(st[i])
#         char_set[idx] += 1
#
#         if(i == len(st)-1):
#             res.append(st[i])
#             res.append(str(char_set[idx]))
#
#         elif(st[i] != st[i+1]):
#             res.append(st[i])
#             res.append(str(char_set[idx]))
#             char_set[idx] = 0
#
#     com = ''.join(res)
#
#     if not len(com) < len(st):
#         return st
#     else:
#         return com


# Solution 2: best solution, less redundancy and complexity is O(n)

def strCompression(st):
    res = []
    reps = 0

    for i in range(len(st)):
        # when a new char rep starts
        if (i != 0) and (st[i-1] != st[i]):
            res.append(st[i-1] + str(reps))
            counter = 0

        counter += 1

    # this because, in the loop previous reps are appended
    res.append(st[-1] + str(reps))


st = "aabcccccaaa"
print(strCompression(st))
