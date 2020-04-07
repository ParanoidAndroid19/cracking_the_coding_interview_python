#
# Solution 1: Brute Force Solution
#
# For every n steps there are 3 options (3 paths):
# 	- 1 hops (n-1)
# 	- 2 hops (n-2)
# 	- 3 hops (n-3)
#
# We can get up to the nth step (reach the top of nth step) by any of the following:
# 	- Going to the (n - l)st step and hopping 1 step.
# 	- Going to the (n - 2)nd step and hopping 2 steps
# 	- Going to the (n - 3)rd step and hopping 3 steps.
#
#
# Therefore, we just need to add the number of these paths together. Because there are option,
# that is kid can do 1, 2 OR 3 hops, we add all the paths.
#
# countWays(0) would mean n==0, that is the kid hopped all the n steps and now has reached
# the top of n steps. And therefore when n==0, we return 1 which means the last hop.
#
# countWays(-ve) would mean n is -ve that is the no. of hops exceeds the no. of steps,
# and thus is not a valid hop/move, therefore here we return 0.
#
# Like the Fibonacci problem, the runtime of this algorithm is exponential (roughly 0(3^n)),
# since each call branches out to three more calls.

# def countWays(n):
#     if n<0:
#         return 0
#
#     elif n==0:
#         return 1
#
#     else:
#         return countWays(n-1) + countWays(n-2) + countWays(n-3)
#
#
# print(countWays(3))


# Solution 2: Memoized solution

def countWays(n):

    if n in ways:
        return ways[n]

    elif n<0:
        ways[n] = 0
        return 0

    # elif n==0:
    #     return 1

    else:
        w = countWays(n-1) + countWays(n-2) + countWays(n-3)
        ways[n] = w
        return w


ways = {0: 1}

print(countWays(5))
