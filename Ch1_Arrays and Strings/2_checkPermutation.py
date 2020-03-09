
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# str2 is permutation of str1, if str2 contains only the chars from str1 and no other char, also the char is repeated 
# the same no. of times. Eg: 'ssim' and 'imsss', str2 is not a permuation of str1 cause it contains an extra 's'

from collections import defaultdict

def isPermutation(str1, str2):

    d = defaultdict(int)

    # obviously both the strings should be of same length
    if len(str1) != len(str2):
        return False

    # set elemenates duplicates, so if str2 uses any new char which is not present in str1 or vice versa, then
    if len(set(str1)) != len(set(str2)):
        return False

    # using defaultdict here, cause calling d[c] where c is not present in d doesn't raise an error,
    # instead for any key not present in d, it returns the default value of 0.
    for c1 in str1:
        d[c1] = d[c1] + 1

    for c2 in str2:
        if d[c2] == 0:
            return False

        d[c2] = d[c2] - 1

    return True

print(isPermutation("mom", "mno")) # The result would be False
