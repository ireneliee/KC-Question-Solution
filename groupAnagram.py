class Solution(object):
    def groupAnagrams(self, strs):
        word_dict = {}
        for item in strs:
            char_list = list(item)
            char_list.sort()
            char_tuple = tuple(char_list)

            if char_tuple not in word_dict:
                word_dict[char_tuple] = []

            word_dict[char_tuple].append(item)
        
        print(word_dict)

        result = list(word_dict.values())
        return result

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))