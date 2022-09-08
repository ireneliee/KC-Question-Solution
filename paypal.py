import math

def getMostVisited(n, sprints):
    run_map = {}
    for i in range(1, n + 1):
        run_map[i] = 0
    
    for i in range(len(sprints) - 1):
        start = sprints[i]
        end = sprints[i + 1]

        if start < end:
            for j in range(start, end + 1):
                
                curr = run_map[j]
                run_map[j] = curr + 1
        elif end < start:
            for j in range(start, end - 1, -1):
                # print(str(j))
                curr = run_map[j]
                run_map[j] = curr + 1

    curr_max = 0
    result = 0
    for i in range(1, n + 1):
        curr = run_map[i]
        if curr > curr_max:
            curr_max = curr
            result = i
    return result


print(getMostVisited(5,[2,4,1,3]))

