class TimeMap:

    def __init__(self):
        self.timemap_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap_dict:
            self.timemap_dict[key] = [{}, timestamp, timestamp]
        
        self.timemap_dict[key][0][timestamp] = value
        self.timemap_dict[key][2] = timestamp


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timemap_dict:
            return ""
        else:
            curr_dict = self.timemap_dict[key][0]

        if timestamp in curr_dict:
            return curr_dict[timestamp]
        else:
            min_timestamp = self.timemap_dict[key][1]
            max_timestamp = self.timemap_dict[key][2]
            if timestamp is None:
                return curr_dict[max_timestamp]
            elif timestamp < min_timestamp:
                return ""
            elif min_timestamp < timestamp < max_timestamp:
                return curr_dict[min_timestamp]
            else: 
                return curr_dict[max_timestamp]

obj = TimeMap()
obj.set("a", "bar", 1)
obj.set("x", "b", 3)
print(obj.get("b", 3))
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))


        


