
import itertools

# Consider the example of 'ab'

def permutations(target, ch):
    perm = []
    l = len(target)

    # first target is 'a', since the length is 1, perm = [['a'], ['a']]
    perm.extend([target[:] for i in range(l+1)])
    i = 0

    # here ch is 'b', first b is inserted at pos 0 then at pos 1
    for p in perm:
        p.insert(i, ch)
        i = i + 1

    # perm = [['b', 'a'], ['a', 'b']]
    return perm


def helper(init, ii):
    newer = []
    for word in init:
        newer = newer + permutations(word, li[ii])

    return newer



str1 = "ab"
li = [s for s in str1]

# stage = [['a']]
stage = [[str1[0]]]

# for each character in the string
for ii in range(1, len(li)):
    stage = helper(stage, ii)


print(stage)
print(len(stage))

# Just to confirm my answer
actualAns = [list(x) for x in itertools.permutations(str1)]
print(sorted(stage) == sorted(actualAns))
