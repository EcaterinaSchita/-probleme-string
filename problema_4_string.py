a=str(input(' introdu primul cuvant '))
b=str(input(' introdu al doilea cuvant '))
c=str(input('introdu al treilea cuvant'))
d=str(input('introdu al patrulea cuvant'))
if len(a)>=3 and len(b)>=3 and len(c)>=3 and len(d)>=3:
    e=a[0]+a[1]+b[0]+b[1]+c[0]+c[1]+c[2]
    for i in range (len(d)//2):
        e+=d
    print('cuvintele sunt' , a,b,c,d)  
    print('cuvantul nou este' , e)  
else:
    print('nu este posibil')    