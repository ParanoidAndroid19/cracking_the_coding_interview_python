
def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))


# fr == initial tower
# to == destination tower
# spare == 3rd, spare tower
def tower(n, fr, to, spare):
    # According to the condition: Only one disk can be moved at a time.
    if n == 1:
        printMove(fr, to)

    else:
        # moving n-1 disks from "fr" to "spare"
        tower(n-1, fr, spare, to)

        # moving the remaining 1 disk from "fr" to "to"
        tower(1, fr, to, spare)

        # moving the n-1 disks from "spare" to "to"
        tower(n-1, spare, to, fr)


tower(3, 'A', 'C', 'B')
