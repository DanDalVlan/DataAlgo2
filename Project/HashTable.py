# Creating a custom hash table as per the requirements of Task 2.A.
# Referenced code from YouTube video uploaded by user @OGGIAI
class HashTable:
    def __init__(this_hash_table):
        this_hash_table.hash_table = []
        this_hash_table.length = 40
        for i in range(this_hash_table.length):
            this_hash_table.hash_table.append([])

    # Function that hashes the key and returns a hash_value
    def _get_hash(this_hash_table, key):
        hash_value = hash(key) % this_hash_table.length
        return hash_value

    # Function that takes in a key and a value, hashes the key, and then adds that key/value pair into the hash table
    def insert(this_hash_table, key, value):
        # Getting the hashed key and the key/value pairing
        key_hash = this_hash_table._get_hash(key)
        key_value = [key, value]
        # Checks to see if the hash bucket is empty, if so, it adds the key/value pairing
        if this_hash_table.hash_table[key_hash] is None:
            this_hash_table.hash_table[key_hash] = list([key_value])
            return True
        # If not, it checks to see if that key/value pair is already in the hash bucket
        else:
            for pair in this_hash_table.hash_table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # If not, it appends that key/value pair into the occupied hash bucket
            this_hash_table.hash_table[key_hash].append(key_value)
            return True

    # Function that takes in a key and returns the value if it exists in the hash table
    def get(this_hash_table, key):
        key_hash = this_hash_table._get_hash(key)
        if this_hash_table.hash_table[key_hash] is not None:
            for pair in this_hash_table.hash_table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Function that takes in a key and deletes that key/value pair from the hash table if it exists
    def delete(this_hash_table, key):
        key_hash = this_hash_table._get_hash(key)

        if this_hash_table.hash_table[key_hash] is None:
            return False
        for i in range(0, len(this_hash_table.hash_table[key_hash])):
            if this_hash_table.hash_table[key_hash][i][0] == key:
                this_hash_table.hash_table[key_hash].pop(i)
                return True
