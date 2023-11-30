// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// This program is written by Mustapha Chriet

@SCREEN
D=A
@addr
M=D  // addr = 16384

@8192
D=A 
@n 
M=D // n = 8191

(LOOP)
@0
D=A
@i 
M=D // i = 0

@KBD 
D=M 
@Black
D;JNE

(White)
@n
D=M 
@i 
D=D-M 
@LOOP 
D;JEQ
@i 
D=M 
@addr 
A=D+M 
M=0
@i 
M=M+1
@White
0;JMP

(Black)
@n
D=M 
@i 
D=D-M 
@LOOP 
D;JEQ
@i 
D=M 
@addr 
A=D+M 
M=-1
@i 
M=M+1
@Black
0;JMP