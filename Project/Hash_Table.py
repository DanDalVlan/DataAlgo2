class Hash_Table:
    def __init__(this_hash_table):
        this_hash_table.hash_table = []
        this_hash_table.length = 40
        for i in range(this_hash_table.length):
            this_hash_table.hash_table.append([])

    def _get_hash(this_hash_table, key):
        hash_value = hash(key) % this_hash_table.length
        return hash_value

    def insert(this_hash_table, key, value):
        key_hash = this_hash_table._get_hash(key)
        key_value = [key, value]

        if this_hash_table.hash_table[key_hash] is None:
            this_hash_table.hash_table[key_hash] = list([key_value])
            return True
        else:
            for pair in this_hash_table.hash_table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            this_hash_table.hash_table[key_hash].append(key_value)
            return True

    def get(this_hash_table, key):
        key_hash = this_hash_table._get_hash(key)
        if this_hash_table.hash_table[key_hash] is not None:
            for pair in this_hash_table.hash_table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(this_hash_table, key):
        key_hash = this_hash_table._get_hash(key)

        if this_hash_table.hash_table[key_hash] is None:
            return False
        for i in range(0, len(this_hash_table.hash_table[key_hash])):
            if this_hash_table.hash_table[key_hash][i][0] == key:
                this_hash_table.hash_table[key_hash].pop(i)
                return True
        
    def print(this_hash_table):
        for item in this_hash_table.hash_table:
            if item is not None:
                print(str(item))
