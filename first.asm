.data
a 192
b 193
.start
LDI 1 ;wczytanie programu
OUT
STA a ; zapisywanie do pamieci
STA b ;zapisywanie do pamieci drugiej liczby
loop:
ADD a
STA a
OUT

ADD    b
STA b
OUT
JMP loop