import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    splitted_array = line.split()
    num_array = splitted_array[0]
    
    operation_array = splitted_array[1]

    num_array_index = 0

    curr_sum = 0
    curr_string_concat = ""

    for i in range(len(operation_array)):
        print('when i is ' + str(i))
        if operation_array[i] == '+':
            curr_sum = curr_sum + int(curr_string_concat)
            curr_string_concat = ""
            print('after adding curr sum is ' + str(curr_sum))
        elif operation_array[i] == '-':
            curr_sum = curr_sum - int(curr_string_concat)
            curr_string_concat = ""
            print('after minusing curr sum is ' + str(curr_sum))
        else:
            curr_string_concat = curr_string_concat + num_array[num_array_index]
            num_array_index = num_array_index + 1
            print('concatenating, currently curr_string_concat is ' +str(curr_string_concat))
            
    if curr_string_concat != "":
        curr_sum = curr_sum + int(curr_string_concat)
    print(curr_sum)


