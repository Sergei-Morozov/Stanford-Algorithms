"""
Bloom filters
-space efficient
-array of n bits
-k hash functions set array bits to 1
- Number of bytes to use and number of hash functions to use is determined
     by array size and false-postive rate
"""

def hash1(key):
    return key % 19

def hash2(key):
    return key % 7

def hash3(key):
    return key % 3

class BloomFilter:
    """
    Realisation with use of 3 hash functions and 20 bit array
    """
    def __init__(self, size = 20):
        self._data = [False for _ in range(size)]
        self._size = size

    def put(self, key):
        """
        set multiple hash bits to true
        """
        idx1 = hash1(key)
        idx2 = hash2(key)
        idx3 = hash3(key)
        self._data[idx1] = True
        self._data[idx2] = True
        self._data[idx3] = True

    def contain(self, key):
        """
        check if multiple hash bits is true
        """
        idx1 = hash1(key)
        idx2 = hash2(key)
        idx3 = hash3(key)
        return bool(self._data[idx1] and self._data[idx2] and self._data[idx3])

    def __repr__(self):
        return str(self._data)


bloom = BloomFilter()
bloom.put(3)
print(bloom)
print(bloom.contain(3))
bloom.put(4)
print(bloom)
print(bloom.contain(4))
bloom.put(5)
print(bloom)
print(bloom.contain(5))

for i in range(20):
    print(f"Index: {i} - bloom {bloom.contain(i)}")
