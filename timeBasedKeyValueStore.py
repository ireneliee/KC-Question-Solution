from collections import deque
import copy

class TimeMap(object):

    def __init__(self):
        self._time_dict = {}

    def set(self, key, value, timestamp):
        new_pq = None
        if key in self._time_dict:
            new_pq = self._time_dict[key]
            
        else:
            new_pq = deque()

        new_pq.appendleft((timestamp, value))
        self._time_dict[key] = new_pq
        print('---printing--------')
        for k in self._time_dict:
            print('Key is : ' + k + ' value is ' + str(self._time_dict[k]))

    def get(self, key, timestamp):
        if key not in self._time_dict:
            return ""
        else:
            pq = self._time_dict[key]

            for item in pq:
                if item[0] <= timestamp:
                    return item[1]
                
            return ""

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)  #// store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))        #// return "bar"
print(timeMap.get("foo", 3))         #// return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4) #// store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         #// return "bar2"
print(timeMap.get("foo", 5))         #// return "bar2"