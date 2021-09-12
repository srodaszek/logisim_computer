numbers=[]
i=0
while i <128:
  
    digits=str(i)
    result=""
    for j in range(4-len(digits)):
        result+="0"
    result+=digits+"\n"
    numbers.append(result)
    i+=1
i=-128
while i<0:
    i*=-1
    digits=str(i)
    result="1"
    for j in range(3-len(digits)):
        result+="0"
    result+=digits+"\n"
    numbers.append(result)
    i*=-1
    i+=1


file=open("display.data","w")
file.write("v2.0 raw\n")
for i in numbers:
    file.write(i)