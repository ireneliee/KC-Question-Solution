# what an elegant brute force ways of doing something

def shrinkingNumberLine(points, k):
    points.sort()
    ret = points[-1] - points[0]
    for i in range(len(points) - 1):
        firstInc = points[0] + k
        thisInc = points[i] + k
        nextDec = points[i+1] - k
        lastDec = points[-1] - k
        
        diff = max(lastDec, thisInc) - min(nextDec, firstInc)
        ret = min(ret, diff)
        
    return ret