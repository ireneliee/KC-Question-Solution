class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return [""]
        result = []
        no_dict = {}
        no_dict['2'] = ['a', 'b', 'c']
        no_dict['3'] = ['d', 'e', 'f']
        no_dict['4'] = ['g', 'h', 'i']
        no_dict['5'] = ['j', 'k', 'l']
        no_dict['6'] = ['m', 'n', 'o']
        no_dict['7'] = ['p', 'q', 'r', 's']
        no_dict['8'] = ['t', 'u', 'v']
        no_dict['9'] = ['w', 'x', 'y', 'z']

        def add(currRes, i):
            if i >= len(digits):
                result.append(currRes)
                return
            
            to_add = no_dict[digits[i]]

            for j in range(len(to_add)):
                add(currRes + to_add[j], i + 1)
        
        add('', 0)

        return result

s = Solution()
digits = "23"
print(s.letterCombinations(digits))