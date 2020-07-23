#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Albina Tileubergen-Thomas and group help'


class Node:
    """ It's container to store key values in a hashtable.  """

    def __init__(self, key, value=None):
        """ Takes the key required and a value which is not """
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """ Repr does returns string """
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """ this method allows the key values to be compared """
        return self.key == other.key


class NoDict:
    """ Creating python dictionary, without using python methods to create the dictionary """

    def __init__(self, num_buckets=10):
        """ If number of buckets wasn't provide, it will be by default 10. """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """ It has to accept key, value and create new node and stores in a bucket. """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for kv in bucket:
            if kv == new_node:
                bucket.remove(kv)
                break
        bucket.append(new_node)

    def get(self, key):
        """ Accepts just one parameter, if key dosn't exist will raise Keyerror  """
        key_value = Node(key)
        bucket = self.buckets[key_value.hash % self.size]
        for kv in bucket:
            if kv == key_value:
                return kv.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """ Method that allows to use square-bracket notation to look the value. """
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """ Method that allows to use square bracket notation to set value of a key """
        self.add(key, value)
