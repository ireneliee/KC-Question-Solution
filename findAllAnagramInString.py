from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_of_anagram = len(p)
        len_of_string = len(s)

        if len_of_anagram > len_of_string:
            return result

        anagram_dict = {}
        string_dict = {}
        for i in range(len_of_anagram):
            anagram_dict[p[i]] = anagram_dict.get(p[i], 0) + 1
            string_dict[s[i]] = string_dict.get(s[i], 0) + 1

        if anagram_dict == string_dict:
            result.append(0)
        
        print('Current anagram dict is ' + str(anagram_dict))
        print('Current string dict is ' + str(string_dict))

        l = 0
        
        for r in range(len_of_anagram, len_of_string):
            print('l is ', str(l))
            print('r is ', str(r))
            print('Before dict is ' + str(string_dict))
            string_dict[s[l]] = string_dict[s[l]] - 1
            string_dict[s[r]] = string_dict.get(s[r], 0) + 1
            

            if string_dict[s[l]] == 0:
                string_dict.pop(s[l])
            
            if string_dict[s[r]] == 0:
                string_dict.pop(s[r])
            
            print('After dict is ' + str(string_dict))

            if anagram_dict == string_dict:
                result.append(l + 1)
            
            l = l + 1
        
        return result



        


sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p))

        
