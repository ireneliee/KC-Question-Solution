def cardinalitySort(nums):
    result = []
    
    one_dic = {}
    for item in nums:
        print('item is '+ str(item))
        count = 0
        binary_rep = bin(item)
        for i in range(len(binary_rep)):
            if binary_rep[i] == '1':
                count = count + 1
        if count in result:
            print('a getting count in ' +str(count))
            one_dic[count].append(item)
        else:
            print('b getting count in ' +str(count))
            one_dic[count] = [item]
    print(one_dic)
    list_of_keys = list(one_dic.keys())
    list_of_keys.sort()
    
    for key in list_of_keys:
        curr = one_dic[key]
        curr.sort()
        for item in curr:
            result.append(item)
    return result

print(cardinalitySort([1,2,3,4,5]))