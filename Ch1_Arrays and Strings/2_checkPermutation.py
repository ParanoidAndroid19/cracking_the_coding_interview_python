
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

from collections import defaultdict

def isPermutation(str1, str2):

    d = defaultdict(int)

    if len(str1) != len(str2):
        return False

    if len(set(str1)) != len(set(str2)):
        return False

    # using defaultdict here, cause calling d[c] where c is not present in d doesn't raise an error,
    # instead for any key not present in d, it returns the default value of 0.
    for c1 in str1:
        d[c1] += 1

    for c2 in str2:
        if d[c2] == 0:
            return False

        d[c2] -= 1

    return True

print(isPermutation("mom", "mno"))
