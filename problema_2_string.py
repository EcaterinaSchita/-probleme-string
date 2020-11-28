a=str(input('introdu sirul'))
m=0
c=0
s=0
for i in a:
    if ord(i) in range (65,91):
        m+=1
    if ord(i) in range (48,58):
        c+=1
    if ord(i) in range(33,48)  :
        s+=1
print('numarul de majuscule este',m)     
print('numarul de cifre este' , c)     
print('numarul de caractere speciale este' ,s)  