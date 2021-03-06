#!C:/Users/Bartosz/AppData/Local/Programs/Python/Python39/python.exe
import sys
import re
def delete_comments(file):
    i=0
    result=[]
    while i<len(file):
        if file[i]=="" or re.search("^\s*$",file[i]): #skip blank lines
            i+=1
            continue 
        temp=file[i].split(';')[0] #erasing comments
        temp=" ".join(temp.split()) # erasing duplicate whitespaces
        result.append(temp)
        i+=1
    return result

def find_flags(file):
    i=0
    global flags
    result=[]
    for line in file:
        if re.search(":$",line):
            if line[0:len(line)-1] in flags.keys():
                print("Duplicate flag"+line[0:len(line)-1])
                exit(0)
            else:
                flags[line[0:len(line)-1]]=i
        else:
            result.append(line)
            i+=1
    return result
        

def split_file(file):
    result=[]
    for line in file:
        
        for word in line.split():
            result.append(word)
    return result

def translate_number(number):
    temp=hex(number)[2::]
    result=""
    for x in range(2-len(temp)):
        result="0"+result
    result=result+temp+'\n'
    return result

def translate_file(file):
    result=[]
    global flags, variables
    for line in file:
        if line in flags.keys():
            result.append(translate_number(flags[line]))
        elif line in variables.keys():
            result.append(translate_number(int(variables[line])))
        elif  re.search("^\d*$",line):
            result.append(translate_number(int(line)))
        elif line.upper()=="ADI":result.append("01\n")
        elif line.upper()=="ADD":result.append("02\n")
        elif line.upper()=="JMP":result.append("03\n")
        elif line.upper()=="OUT":result.append("04\n")
        elif line.upper()=="STA":result.append("05\n")
        elif line.upper()=="LDI":result.append("06\n")
        elif line.upper()=="LDA":result.append("07\n")
        elif line.upper()=="JZ":result.append("08\n")
        elif line.upper()=="SBI":result.append("09\n")
        elif line.upper()=="SUB":result.append("0a\n")
        elif line.upper()=="JS":result.append("0b\n")
        elif line.upper()=="JC":result.append("0c\n")
        elif line.upper()=="PUSH":result.append("0d\n")
        elif line.upper()=="POP":result.append("0e\n")
        elif line.upper()=="HLT":result.append("ff\n")
        elif line.upper()=="NOP":result.append("00\n")
        else:
            print("Not recognized command: "+line)
            exit(4)
    return result

def find_variables(file):
    result=[]
    global variables
    if file[0]==".start":
        i=1
        while i<len(file):
            result.append(file[i])
            i+=1
        return result
    else:
        i=1
        while i<len(file):
            if file[i]==".data":
                i+=1
                continue
                
            elif file[i]==".start":
                i+=1
                while i<len(file):
                    result.append(file[i])
                    i+=1
                return result
            else:
                temp=file[i].split()
                variables[temp[0]]=int(temp[1])
                i+=1

def translate_variables(file):
    global variables
    for key in variables.keys():
        file.append(str(variables[key]))
        variables[key]=len(file)-1
    return file



flags=dict()
variables=dict()


if len(sys.argv)==0:
    print("Pass file name")
    exit(1)
try:
    _file=open(sys.argv[1],"r")
    file=_file.read()
    _file.close()
except:
    print("Couldn't open file")
    exit(2)

file=file.split('\n')
file=delete_comments(file)
file=find_variables(file)

file=split_file(file)
file=find_flags(file)
file=translate_variables(file)
file=translate_file(file)
print(file)

if (len(sys.argv)>2):
    filename=sys.argv[2]
else:
    filename=".\\a.out"

result_file=open(filename,"w")
result_file.write("v2.0 raw\n")
for line in file:
    result_file.write(line)

