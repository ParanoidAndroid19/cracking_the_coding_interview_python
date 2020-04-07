
# Solution 1: Brute force solution. O(N) since the whole list need to be traversed.

# def magic(li):
#
#     for i in range(0, len(li)):
#         if li[i] == i:
#             return i
#
#     return "No magic index"
#
#
# li = [42, 3, 2, 5, 9]
# print(magic(li))


# Solution 2: Uses the concept of binary search. Since here we have a sorted list of distinct integers,
# the problem can be reduced in half recursively. The time complexity is O(log N).

def magic(first, last):

    mid = (first + last)//2

    if first > last:
        return "Not Found"

    #base case
    if li[mid] == mid:
        return mid

    else:
        if mid < li[mid]:
            # consider first half
            return magic(first, mid-1)
        else:
            # consider latter half
            return magic(mid+1, last)


li = [-14, -12, 0, 1, 3, 5, 20, 23]

f = 0
l = len(li) - 1

print(magic(f, l))
