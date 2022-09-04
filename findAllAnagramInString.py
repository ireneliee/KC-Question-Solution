from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_of_anagram = len(p)
        len_of_string = len(s)

        sorted_char_list = list(p)
        sorted_char_list.sort()

        def anagramTest(s1):
            s1 = list(s1)
            s1.sort()

            return s1 == sorted_char_list
        
        # sliding window
        start = 0
        end = len_of_anagram

        while end <= len_of_string:
            curr_str = s[start: end]
            if anagramTest(curr_str):
                result.append(start)
                while True:
                    end = end + 1
                    if end < len_of_string and s[start] == s[end - 1]:
                        start = start + 1
                        result.append(start)
                    else:
                        start = start + 1
                        break
            else:
                start = start + 1
                end = end + 1

        
        return result


sol = Solution()
s = "abab"
p = "ab"
print(sol.findAnagrams(s, p))

        
