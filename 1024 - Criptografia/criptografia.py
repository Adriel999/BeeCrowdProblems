from math import ceil 

#Number of lines
n = int(input())

#Cryptography
for i in range(n):
    inp = str(input())
    
    #First step
    out = ''
    for char in inp:
        if char.isalpha():
            out += chr(ord(char)+3)
        else:
            out += char

    #Second step
    out = out[::-1]
    
    #Third step
    x = ceil(len(out)/2)
    crip = ''
    for char in out[-x:]:
        crip += chr(ord(char) - 1)
    out = out.replace(out[-x:], crip)
    print(out)