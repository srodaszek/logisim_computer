numbers=[]
for i in range(256):
    digits=str(i)
    result=""
    for j in range(3-len(digits)):
        result+="0"
    result+=digits+"\n"
    numbers.append(result)
file=open("display.data","w")
file.write("v2.0 raw\n")
for i in numbers:
    file.write(i)