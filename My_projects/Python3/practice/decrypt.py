import crypt
from hmac import compare_digest as compare_hash

plaintext = 'root'
hashed = crypt.crypt(plaintext)
if not compare_hash(hashed, crypt.crypt(plaintext, hashed)):
    raise ValueError("hashed version doesn't validate against original")
