
# Solution 1: The Obvious Straightforward sol and incredibly naive
# So here I just have to check if any permuation of the given string is a palindrome. If it is then return True.
# So here I obviously have to use itertools. I will first create a list of all the permuations and then for each ele in the list I'll check if its a palindrome.
# Since there are way too many permutations, I will only consider those strings which begin and end with same char and have blank space at the same index as the original string.
# Also having spaces in the str will cause problems while finding palindromes. So convert it to list so that can elemenate the ' '.

# from itertools import permutations
#
# def isPalindrome(st1, l):
#
#     st1.remove(' ')
#
#     if(l%2==0):
#         r = l//2
#     else:
#         r = l//2 + 1
#
#     for i in range(0, r):
#         if(st1[i] != st1[-i-1]):
#             return False
#
#     return True
#
#
# def palindromePermutation(st):
#
#     perms = [x for x in permutations(st)]
#     l = len(st)
#
#     for s in set(perms):
#         if(s[0] == s[-1] and s[4] == ' '):
#             if(isPalindrome(list(s), l) == True):
#                 print(s)
#                 return True
#
#     return False



# Solution 2: Short cut ans
# To check if any permutation of a string is a palindrome, we just make dictionary and record the char and
# its frequency in the string. For the string to have possible palindome in its permutations, all the freq
# should be even (since palindrom has pairs of chars), if the str len is odd then there must be only one
# char with odd freq (since that would be the char in the middle)

def palindromePermutation(st):

    li = list(st)

    while ' ' in li:
        li.remove(' ')

    odd = 0

    dict = {k: 0 for k in li}
    l = len(li)

    for c in li:
        dict[c] = dict[c] + 1

    # if len of string is even
    for k in dict:

        # if freq of a char in str is odd
        if(dict[k]%2!=0):
            odd = odd + 1

            # len of str (without spaces, considering only chars) is even
            if(l%2==0):
                return False

    # if len of str is odd and there is more then or less than 1 char whose freq is odd
    if(l%2!=0 and odd != 1):
        return False


    return True

# red rum sir is murder
st = "sed rum rir is rurdem"
print(palindromePermutation(st.lower()))
