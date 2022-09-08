arr = [[1,7], [5,11], [7,9]]
dic = {}

for i in range(len(arr) - 1):
    # curr and the next one
    if arr[i][0] < arr[i + 1][0]:
        dic[(arr[i], arr[i + 1] - 1)] = 1
    