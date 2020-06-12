class LRU_Cache:

	def __init__(self, capacity):
		self.capacity = capacity
		self.cache_map = {}

	def get(self, key=None):
		if key is None:
			print("Please insert the key.")
			return

		if key in self.cache_map:
			value = self.cache_map[key]
			self.cache_map.pop(key)
			self.cache_map[key] = value
			return value
		return -1

	def set(self, key=None, value=None):
		if key is None:
			print("Please insert the key.")
			return
		elif value is None:
			print("Please insert the value.")
			return
			
		if key in self.cache_map:
			self.cache_map.pop(key)
			self.cache_map[key] = value
		else:
			if len(self.cache_map) == self.capacity:
				self.cache_map.pop( list(self.cache_map.keys())[0])
			self.cache_map[key] = value

print("create a new LRU Cache with capatity 5")
our_cache = LRU_Cache(5)

print("add value 1 with key 1")
our_cache.set(1, 1);
print("add value 2 with key 2")
our_cache.set(2, 2);
print("add value 3 with key 3")
our_cache.set(3, 3);
print("add value 1 with key 1")
our_cache.set(4, 4);

print("retrieve key 1")
print(our_cache.get(1))       # returns 1
print("retrieve key 2")
print(our_cache.get(2))       # returns 2
print("retrieve key 9")
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

print("add value 5 with key 5")
our_cache.set(5, 5)
print("add value 6 with key 6")
our_cache.set(6, 6)

print("retrieve key 3")
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("corner case 1, empty key when setting")
our_cache.set(value = 3)

print("corner case 1, empty key when retrieving")
our_cache.get()

print("corner case 1, empty value when setting")
our_cache.set(1)