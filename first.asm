XD:
LDI    1 ;wczytanie programu
OUT
STA 192 ; zapisywanie do pamieci
STA 193 ;zapisywanie do pamieci drugiej liczby
loop:
ADD 192
STA 192
OUT

ADD    193
STA 193
OUT
JMP loop