
#start list 1

unsortedList1 = [89,23,33,45,10,12,45,45,45]


# loop through entire unsorted list
for i in range(0, len(unsortedList1)):
    # don't go past the length of list
    for j in range(len(unsortedList1) - 1):
        # if current value is bigger than next value
        if (unsortedList1[j] > unsortedList1[j + 1]):
            # switch out the value locations
            unsortedList1[j], unsortedList1[j + 1] = unsortedList1[j + 1], unsortedList1[j]


print(unsortedList1)

#start list 2

unsortedList2 = [67,45,2,13,1,998]

# loop through entire unsorted list
for i in range(0, len(unsortedList2)):
    # don't go past the length of list
    for j in range(len(unsortedList2) - 1):
        # if current value is bigger than next value
        if (unsortedList2[j] > unsortedList2[j + 1]):
            # switch out the value locations
            unsortedList2[j], unsortedList2[j + 1] = unsortedList2[j + 1], unsortedList2[j]


print(unsortedList2)
