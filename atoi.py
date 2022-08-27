class Solution:
    def myAtoi(self, s: str) -> int:
        numb = ""
        isNegative = False
        isInvalid = False
        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57:
                numb = numb + s[i]
            elif s[i] == '-':
                isNegative = True
            elif (s[i] < 48 or s[i] > 57) and numb == "":
                isInvalid = True
        
        if isInvalid:
            return 0
        if isNegative:
            numb_result = int(numb) * -1
        else:
            numb_result = int(numb)
        # [-231, 231 - 1]   

        if numb_result < -1 * pow(2,31):
            return pow(2,31) * -1
        elif numb_result > pow(2, 31):
            return pow(2, 31)

        return numb_result

sol = Solution()
s = "4193 with words"
print(sol.myAtoi(s))