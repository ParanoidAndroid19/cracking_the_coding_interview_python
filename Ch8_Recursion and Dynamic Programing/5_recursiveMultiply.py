
# 8.5) Recursive Multiply: Write a recursive function to multiply two positive integers without using
# the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the
# number of those operations.

# Solution 1: simple recursive method

# def multiply(a, b):
#     if b == 1:
#         return a
#
#     else:
          # multiplication is just repeated addition. Eg: 2 * 3 = 2 + 2 + 2 = 6
#         return a + multiply(a, b-1)
#
#
# print(multiply(6, 7))


# Solution 2: Caching results to avoid duplicate recursive calls, memoization technique
# trading space complexity for time complexity

def multiply(a, b):
    if b == 1:
        return a
    else:
        # multiplication is just repeated addition. Eg: 2 * 3 = 2 + 2 + 2 = 6
        return a + multiply(a, b-1)


def recMul(p, q):
    # to reduce the number of recursive calls, keep t as the smaller integer.
    # Consider, 2 * 10 here if t = 10 then there would be 5 recursive calls since b = t//2 = 5
    # where as if t = 2 then there would be one recursive call b = 2//2 = 1
    if p < q:
        t = p
        a = q
    else:
        t = q
        a = p

    # using dictionary to record results
    dict = {}

    # Calculating only half of the answer, i.e for 3 * 4, recursively calculating 3 * (4//2) = 3 * 2 = 6
    dict[t//2] = multiply(a, t//2)

    # then adding the half sols to get complete sol. dict[4//2] = dict[2] = 6
    # Thus, 3 * 4 = dict[2] + dict[2] = (3 * 2) + (3 * 2) = 12
    # Hence, this method saves the duplicate recursive calls used to calculate 3 * 2 again.
    if(t%2==0):
        return dict[t//2] + dict[t//2]

    # When b is odd, consider 3 * 5 = dict[5//2] + dict[5//2] + 3 = dict[2] + dict[2] + 3 = 6 + 6 + 3 = 15
    else:
        return dict[t//2] + dict[t//2] + a

print(recMul(7, 42))
