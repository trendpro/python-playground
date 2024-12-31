# Exploring python hash functions

import hashlib

# hash() function
name = "Kyalo Kitili"
print(hash(name))

# check available algorithms
print(hashlib.algorithms_available)

# check guaranteed algorithms
print(hashlib.algorithms_guaranteed)

# md5 example
print(hashlib.md5(name.encode()).hexdigest())
