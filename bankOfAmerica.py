import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    sum = 0
    for i in range(1, int(line) + 1):
        if i % 5 != 0 and i % 7 != 0:
            sum = sum + i
            print('currently sum is ' + str(sum))
    print(str(sum))