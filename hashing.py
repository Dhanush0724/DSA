tuple_values  = (1,3,5,7,9)
print(str(hash(tuple_values)))
var = (2,4,6,8)
print(hash(var))

import hashlib

string = "hello james"
hash_object_breifcase = string.encode('utf-8')
hash_object = hashlib.sha256()
hash_object.update(hash_object_breifcase)

hex_digit = hash_object.hexdigest()

decode_string = hash_object_breifcase.decode('utf-8')

print(f"Original String: {string}")
print(f"Encoded String (bytes): {hash_object_breifcase}")
print(f"SHA-256 Hash: {hex_digit}")
print(f"Decoded String: {decode_string}")