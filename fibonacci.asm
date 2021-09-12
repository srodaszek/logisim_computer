.data
a 1
b 1
.start
LDA a
OUT
loop:
ADD a
STA a
OUT

ADD    b
STA b
OUT
JMP loop