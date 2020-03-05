#!python

from linkedlist import LinkedList


class HashTable(object):
    '''A hash table that resolves collisions using separate chaining.'''
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
           Best and worst case running time: O(1) because we rely only upon
           another method that is runs in O(1) time, the length of a list which
           takes constant time to calculate, and the division operator.
        """
        # Calculate load factor
        return (self.length() / len(self.buckets))

    def keys(self):
        """Return a list of all keys in this hash table.
           Best and worst case running time: O(n) because the number of
           iterations through the for loop scales with the growth of the number
           of entries in the hash table.
        """
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
           Best and worst case running time: O(n), because the number of
           iterations needed to collect the values will grow in proportion to
           the growth of number of entries in the hash table, at a linear
           magnitude.
        """
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
           Best and worst case running time: O(n) because on each of b
           iterations through the for loop, we require l iterations (the load
           factor, or the average number of entries we can expect to be in each
           bucket), which equal n iterations. This method will therefore scale
           in linear proportion to the size of the number of entries in the
           hash table.
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
           Best and worst case running time: O(1) because we simply return the
           value stored in a property of the calling object.
        """
        # Count number of key-value entries in each of the buckets
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
           Best case running time: O(1) if we find the entry at the head node
           of the bucket it is located in.
           Worst case running time: O(n), if the bucket we index into contains
           all the entries in the hash table, and the entry we are looking for
           is either the tail node or not in that list at all.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
           Best case running time: O(1), because we may need only one iteration
           in the execution of the find method if the key we are looking for is
           located at the head node.
           Worst case running time: O(n), if the bucket we are looking for the
           entry in contains all the key value pairs, and we need to iterate
           through the whole list. This may happen if the item is either the
           tail node or not in the list at all.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
           Best case running time: O(1), if there is already an entry with
           the same value as key (the argument that's been passed into this
           method) present at the head node in the bucket. Or if there are no
           previous nodes in the bucket being traversed through.
           Worst case running time: O(n) if all the items in the hash table are
           in the bucket we index into, and there is not already an entry with
           the same value as key (the argument that has been passed into this
           method) present, or it is at the tail node in that bucket.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
        else:
            # increment the size because we are adding a new key value pair
            self.size += 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
           Best case running time: O(1) if we are deleting an entry that is the
           head node in the bucket that it is located in.
           Worst case running time: O(n) if all the entries are located are the
           same bucket, and the entry we are trying to delete is not present in
           any of the nodes of that bucket.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
           Should be called automatically when load factor exceeds a threshold
           such as 0.75 after an insertion (when set is called with a new key).
           Best and worst case running time: O(n)
           The longest running portion of this method's implementation is the
           for loop at the bottom, which needs to iterate over all pre-existing
           entries in our hash table for the process of rehashing. This step
           will always require n iterations, and therefore will scale in direct
           proportion to the growth of the number of entries in the hash table.
           Best and worst case space usage: O(n), because most of the memory is
           used by the key_value_pairs array, which scales at a linear
           magnitude with respect to the growth of the number of entries.
        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if load factor is low
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # Get a list to temporarily hold all current key-value entries
        key_value_pairs = self.items()
        # Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for i in range(new_size)]
        # reset size
        self.size = 0
        # Rehash each key-value entry into the new list of buckets,
        for key, value in key_value_pairs:
            self.set(key, value)


class HashTableProbing(HashTable):
    '''A hash table that resolves collisions without chaining.'''
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [None for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def keys(self):
        """Return a list of all keys in this hash table.

           Best and worst case running time: O(n) because the number of
           iterations through the for loop scales with the growth of the number
           of entries in the hash table.

        """
        # Collect all keys in each of the buckets
        all_keys = []
        for entry in self.buckets:
            if entry is not None:
                all_keys.append(entry[0])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.

           Best and worst case running time: O(n), because the number of
           iterations needed to collect the values will grow in proportion to
           the growth of number of entries in the hash table, at a linear
           magnitude.

        """
        # Collect all values in each of the buckets
        all_values = []
        for entry in self.buckets:
            if entry is not None:
                all_values.append(entry[1])
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.

           Best and worst case running time: O(n) because on each of b
           iterations through the for loop, we require l iterations (the load
           factor, or the average number of entries we can expect to be in each
           bucket), which equal n iterations. This method will therefore scale
           in linear proportion to the size of the number of entries in the
           hash table.

        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for i in range(len(self.buckets)):
            if self.buckets[i] is not None:
                all_items.append(self.buckets[i])
        return all_items

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.

           Best case running time: O(1) if we find the entry at the index
           determined by the hash algorithm.

           Worst case running time: O(n), where n is the number of items in
           the hash table.

        """
        # if entry is inside, it is either at the hashed index, or right of it
        for i in range(len(self.buckets)):
            entry = self.buckets[i]
            if entry is not None and entry[0] == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.

           Best case running time: O(1), because we may need only one iteration
           in the execution of the find method if the key we are looking for is
           located at the head node.

           Worst case running time: O(n), if the bucket we are looking for the
           entry in contains all the key value pairs, and we need to iterate
           through the whole list. This may happen if the item is either the
           tail node or not in the list at all.

        """
        for entry in self.buckets:
            if entry is not None and entry[0] == key:
                return entry[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.

           Best case running time: O(1) if there is a NoneType object existing
           at the index in the buckets array decided by the hashing algorithm.

           Worst case running time: O(n) when we are performing an update, and
           the entry is at the last index in the hash buckets array.

        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        # place the entry in the index, if no previous entry
        if self.buckets[index] is None:
            self.buckets[index] = (key, value)
            self.size += 1
        # try to find a key with the same as the one being set, then update
        elif self.contains(key) is True:
            for i in range(len(self.buckets)):
                entry = self.buckets[i]
                if entry is not None and entry[0] == key:
                    self.buckets[i] = (key, value)
        # there is a previous entry with a different key, go find another index
        else:
            self.buckets.append((key, value))
            self.size += 1

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.

           Average running time: O(n) because we perform linear search to
           discover if the key exists currently in the hash buckets array.

        """
        for i in range(len(self.buckets)):
            entry = self.buckets[i]
            if entry is not None and entry[0] == key:
                self.buckets[i] = None
                self.size -= 1
                return None
        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTableProbing(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    # print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
