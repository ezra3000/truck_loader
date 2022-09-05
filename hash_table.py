class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.map = []
        for i in range(table_size):
            self.map.append([])

    def add(self, key, item):
        bucket = key % len(self.map)
        bucket_list = self.map[bucket]
        key_value = [key, item]
        bucket_list.append(key_value)

    def get(self, key):
        bucket = key % self.table_size
        bucket_list = self.map[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

