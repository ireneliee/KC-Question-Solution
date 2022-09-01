def removeConflicts(meetings):
    meetings.sort()
    result = []
    prevEnd = meetings[0][1]
    prevStart = meetings[0][0]
    cancelled = 0

    for i in range(1, len(meetings)):
        currStart = meetings[i][0]
        currEnd = meetings[i][1]

        if prevStart <= currStart < prevEnd:
            cancelled = cancelled + 1
            
            #deciding which to remove
            if currEnd < prevEnd:
                prevEnd = currEnd
                prevStart = currStart
    return cancelled

meetings = [[1,2],[1,3],[4,5]]
print(removeConflicts(meetings))