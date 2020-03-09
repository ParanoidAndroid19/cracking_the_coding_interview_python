
# Naive Solution:
# def isUnique(str1):
#     li = []
#     for c in str1:
#         if c in li:
#             return "Not Unique"
#         li.append(c)
#     return "Unique"

# A faster solution but still not the best solution. No nested loops at least.
# def isUnique(str1):
#     dict = {}
#     # one loop to initialize all the char = 0 instances
#     dict = {k: 0 for k in str1}
#
#     # second loop to record the frequency of the char in key: val
#     for c in str1:
#         # first instance of c: 0 + 1
#         dict[c] = dict[c] + 1
#
#         if dict[c] > 1:
#             return "Not Unique"
#
#     return "Unique"

def isUnique(str1):

    # Initialize occurrences of all characters
    # The ASCII table has 128 characters, with values from 0 through 127.
    char_set = [False]*128

    for c in str1:
        val = ord(c) # eg: ord('a') = 97
        
        # For the char in string, its val (index in char_set) is set as True in the char_set
        if char_set[val] == True:
            return "Not Unique"
        
        # Here we set the value as True for chars present in the string
        char_set[val] = True

    return "Unique"


str1 = "lily"
print(isUnique(str1))
