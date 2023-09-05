import heapq

class WordFreq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq != other.freq:
                return self.freq > other.freq
        return self.word < other.word

class Solution(object):
    def topKFrequent(self, words, k):
        result = []
        words_dict = {}
        max_heap = []

        for word in words:
            currTotal = 1
            if word in words_dict:
                currTotal = words_dict[word] + 1
            words_dict[word] = currTotal

        for q, v in words_dict.items():
            heapq.heappush(max_heap, (-v, q))


        while len(result) < k:
            result.append(heapq.heappop(max_heap))

        return [i.word for i in result]

s = Solution()
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(s.topKFrequent(words,k))