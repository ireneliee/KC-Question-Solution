class TimeMap:

    def __init__(self):
        self.timemap_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap_dict:
            self.timemap_dict[key] = {}
            
        self.timemap_dict[key][timestamp] = value

        


    def get(self, key: str, timestamp: int) -> str:
        pass
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)