 	global _start
 	section 	.text
_start:
mov 	rax,0x73e082c863be0000
mov 	rcx,0x886082a864020000 
mov 	rdx,0x829800020000
mov 	rbx,0x80e40000e0800000
mov 	rsi,0xf90f9cc900be0000
mov 	rdi,0x800422a800820000
mov 	rsp,0x3e02a9be0020000
mov 	rbp,0xfaafae02ac800000
mov 	r8,0x600200080aa20000
mov 	r9,0xf9efbe08c9be0000
mov 	r10,0x280020820080000
mov 	r11,0x21ef8200c8000000
mov 	r12,0xf80a80f80f800000
mov 	r13,0x8be01ea3e8000000
mov 	r14,0x802802a0000000
mov 	r15,0x1601e0005800000


mov rax, 60
mov rdi, 0 	
syscall

