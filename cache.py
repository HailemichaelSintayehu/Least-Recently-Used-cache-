class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def getMostRecentValue(self, key):
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def addValue(self, key, value):
        if len(self.cache) >= self.capacity:
            self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value

my_cache = Cache(3)

my_cache.put("key1", "value1")
my_cache.put("key2", "value2")
my_cache.put("key3", "value3")

print(my_cache.get("key1"))  # Output: value2
print(my_cache.get("key2"))  # Output: value2

my_cache.put("key4", "value4")

print(my_cache.get("key3"))  # Output: None
print(my_cache.get("key4"))  # Output: value4
