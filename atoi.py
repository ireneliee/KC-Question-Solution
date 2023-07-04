class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        
        parsed = ""
        foundNum = False
        for car in s:
            if car.isnumeric() or car == "+" or car == "-":
                parsed = parsed + car
                foundNum = True
            else:
                if car == " " and foundNum:
                    break
                elif car != " ":
                    break
        print("Step A: " + parsed)

        if len(parsed) == 0:
            return 0
        
        if len(parsed) >= 2 and not parsed[1].isnumeric():
            return 0
        try:
            result = int(parsed)
        except:
            return 0
        
        print("Step B: " + str(result))

        if result < -2 ** 31:
            result = -2 ** 31
        elif result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        
        return result
        
        
            
        


sol = Solution()
s = "   +0 123"
print(sol.myAtoi(s))