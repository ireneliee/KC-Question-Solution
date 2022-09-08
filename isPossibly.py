def isPossible(a, b, c, d):
    # Write your code here
    def recurse(x, y):
        if x == a and y == b:
            return True
        elif x < a or y < b:
            return False
        else:
            return recurse(x, y - x) or recurse(x - y, y)
    
    result = recurse(c, d)
    print(result)

isPossible(1,2,3,6)