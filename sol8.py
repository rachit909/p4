import sys
import hashlib
import hmac
import base64

data = "Ghidra rocks!"

"""
4e1435fd
ab0792f3
7aae8208
bb09d1d
8d77684f
99695b71
49d153bb
d4880319
"""

mac_addy = hmac.new(b'\xfd\x35\x14\x4e\xf3\x92\x07\xab\x08\x82\xae\x7a\x1d\xd1\x09\xbb\x4f\x68\x77\x8d\x71\x5b\x69\x99\xbb\x53\xd1\x49\x19\x03\x88\xd4', b'Ghidra rocks!', hashlib.sha256)
sys.stdout.buffer.write(len(data).to_bytes(4, 'little') + b'Ghidra Rocks!' + mac_addy.digest())