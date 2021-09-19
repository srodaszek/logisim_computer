.data
a 1
b 1
.start
start:
LDI 1
STA a
STA b
OUT
loop:
ADD a
STA a
JS start
OUT
ADD b
STA b
JS start
OUT
JMP loop
