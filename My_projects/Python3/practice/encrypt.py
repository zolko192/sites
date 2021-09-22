#!/usr/bin/python3

import hashlib
from hashlib import blake2b

m = blake2b()
m.update(b"hello")
print(m.hexdigest())