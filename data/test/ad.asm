; NASM simple program
; Written 11:22 AM Saturday January 31, 2015

section .data

EatMsg: db "Eat at Joe's", 10
EatLen: equ $-EatMsg 

section .text

global _start

_start:
	nop
	mov eax,EatMsg
	mov ebx,EatLen
	int 80h

	mov eax,1
	mov ebx,0
	int 80h
