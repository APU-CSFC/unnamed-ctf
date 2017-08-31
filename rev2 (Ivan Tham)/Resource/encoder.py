#!/usr/bin/env python3

key = sum(ord(i) for i in 'aaooeeuu') % 0xff
dec = 'flag{women_they_are_a_complete_mystery}'
enc = ''.join(chr(ord(c) ^ key) for c in dec)

print(', '.join(f'0x{ord(c):=02x}' for c in enc) + ', 0x00')

# Test decode
assert ''.join(chr(ord(i) ^ key) for i in enc) == dec
