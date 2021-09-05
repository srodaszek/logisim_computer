def parse_command(command):
    
    
    microcode = [ code.strip() for code in command.split('|')]
    result=0
    for code in microcode:
        if code=="DI":result|=1<<0
        elif code=="HLT":result|=1<<1
        elif code=="CO":result|=1<<2
        elif code=="CI":result|=1<<3
        elif code=="CE":result|=1<<4
        elif code=="BI":result|=1<<5
        elif code=="AI":result|=1<<6
        elif code=="EO":result|=1<<7
        elif code=="SUB":result|=1<<8
        elif code=="MA":result|=1<<9
        elif code=="MO":result|=1<<10
        elif code=="MI":result|=1<<11
        elif code=="II":result|=1<<12
        elif code=="AO":result|=1<<13

        elif code=="NOP":pass
    return result

def parse_line(line):
    global memory
    places,command = line.split(':')
    places=places.replace(" ","")
    command=parse_command(command)
    X_pos=[]
    places=places[::-1] #reverse string
    
    for i in range(len(places)):
        if places[i]=="X":
            X_pos.append(i)
            places=places[:i]+"0"+places[i+1:]
        
    places=places[::-1] #reverse string
    place=int(places,2)
    i=0
    while i<2**len(X_pos):
        place_temp=place
        for j in range(len(X_pos)):
            bit=1
            place_temp=(((bit<<j)&i)>>j)<<X_pos[j]|place_temp
            memory[place_temp]=command 
        i+=1



length=16
file=open("commands.txt","r")
memory=[]
for i in range(2**length):
    memory.append(0)


line=file.readline()
while line!="":
    parse_line(line)
    line=file.readline()
file.close()
file=open("ROM.data","w")
file.write("v2.0 raw\n")
for code in memory:
    temp=hex(code)[2::]
    result=""
    for x in range(6-len(temp)):
        result="0"+result
    result=result+temp+'\n'
    file.write(result)