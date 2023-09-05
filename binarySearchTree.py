# After sorting the array we will find the missing elements inside the nums array

nums = [10,6,7,8,25]


# smallest number
# biggest number
def find_smallest_number(johnny):
    missingElement = []
    johnny.sort()

    #[6,7,8,10,25]

    smallest_number = johnny[0]
    biggest_number = johnny[-1]

    for i in range(smallest_number, biggest_number + 1):
        if i not in johnny:
            missingElement.append(i)


    return missingElement

print(find_smallest_number(nums))
