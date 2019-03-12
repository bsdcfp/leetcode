import os
class TimeMap:
    def __init__(self):
        self.tmap = {}
        self.stamp_idx = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int'):
        if not key or not value:
            return None
        if key in self.tmap:
            self.tmap[key][timestamp] = value
        else:
            self.tmap[key] = {timestamp:value}

    def get(self, key: 'str', timestamp: 'int'):
        if key not in self.tmap:
            return None
        else:
            keys = list(self.tmap[key].keys())
            keys.sort()
            prev = 0
            for t in keys:
                if int(t) < timestamp:
                    prev = int(t)
                    continue
                elif int(t) == timestamp:
                    prev = int(t)
                    break
            return "" if prev == 0 else self.tmap[key][prev]

obj = TimeMap()
obj.set('love', 'high', 10)
obj.set('love', 'low', 20)
print(obj.get('love', 5))
print(obj.get('love', 10))
print(obj.get('love', 15))
print(obj.get('love', 20))
print(obj.get('love', 25))
