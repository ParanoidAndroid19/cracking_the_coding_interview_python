
# Solution 1: Getting rid of duplicates in list by checking

# import itertools
#
# def permutations(str):
#     if len(str) <= 0:
#         return None
#     elif len(str) == 1:
#         return [str]
#     elif len(str) == 2:
#         if str == str[::-1]:
#             return [str]
#         else:
#             return [str, str[::-1]]
#
#     else:
#         return combine(str[0], permutations(str[1:]))
#
#
# def combine(char, string_list):
#     output_string_list = []
#
#     for string in string_list:
#         for i in range(len(string) + 1):
#             # output_string_list += [string[0:i] + char + string[i:]]
#             new = [str(string[0:i] + char + string[i:])]
#             if new[0] not in output_string_list:
#                 # if output_string_list != []:
#                 #     print(new.strip() == output_string_list[0].strip())
#                 output_string_list += new
#
#     return output_string_list
#
#
# str1 = 'aab'
# myAns = permutations(str1)
# print(myAns)
#
# # Just to confirm my answer
# actualAns = [''.join(x) for x in itertools.permutations(str1)]
#
# for i in range(len(actualAns)-1, -1, -1):
#     if actualAns[i] in actualAns[:i]:
#         actualAns.pop(i)
#
# print(sorted(myAns) == sorted(actualAns))


# Solution 2: Getting rid of duplicates using dictionary

def permutations(str):
    if len(str) <= 0:
        return None
    elif len(str) == 1:
        return {str: 1}
    elif len(str) == 2:
        return {str: 1, str[::-1]: 1}

    else:
        return combine(str[0], permutations(str[1:]))


def combine(char, string_list):
    output_string_list = {}

    for string in string_list:
        for i in range(len(string) + 1):
            # output_string_list += [string[0:i] + char + string[i:]]
            output_string_list[string[0:i] + char + string[i:]] = 1

    return output_string_list



str1 = 'aab'
myAns = permutations(str1)
print(myAns)
