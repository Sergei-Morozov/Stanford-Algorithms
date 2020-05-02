"""
Hash based on
-linked list
-open addressing (linear probing, double hashing)
"""

def hash(key):
    """
    example hash function (key mod 19)
    """
    return key % 19


class HashMapLinked:
    def __init__(self):
        """
        Init hash map of size 19 buckets, each bucket contains list of
        [key, value]
        """
        self._data = [[] for _ in range(20)]

    def put(self, key, value):
        index = hash(key)
        for item in self._data[index]:
            if item[0] == key:
                item[1] = value
                break
        else:
            self._data[index].append([key,value])

    def get(self, key):
        index = hash(key)
        for item in self._data[index]:
            if item[0] == key:
                return item[1]
    def __repr__(self):
        return str(self._data)

class HashMapOpened:
    def __init__(self, size = 20):
        """
        Init hash map of size 19 buckers with open addressing
        based on [key, value] and probing next slot
        """
        self._data = [None for _ in range(20)]
        self._size =size

    def put(self, key, value):
        index = hash(key)
        if self._data[index] is None:
            self._data[index] = [key, value]
        elif self._data[index][0] == key:
            self._data[index][1] = value
        else:
            while index < self._size:
                index += 1
                if self._data[index] is None:
                    self._data[index] = [key, value]
                    break
                elif self._data[index][0] == key:
                    self._data[index][1] = value
                    break
            else:
                #resize hash
                pass

    def get(self, key):
        index = hash(key)
        while index < self._size:
            if self._data[index] is None:
                return None
            elif self._data[index][0] == key:
                return self._data[index][1]
                break
            index += 1

    def __repr__(self):
        return str(self._data)

hashmap = HashMapLinked()
hashmap.put(1,9)
hashmap.put(19,9)
hashmap.put(2,9)
hashmap.put(21,10)
hashmap.put(21,12)
print(hashmap.get(21))
print(hashmap)



hashmap = HashMapOpened()
hashmap.put(1,9)
hashmap.put(19,9)
hashmap.put(2,9)
hashmap.put(21,10)
hashmap.put(21,12)
print(hashmap.get(21))
print(hashmap)
