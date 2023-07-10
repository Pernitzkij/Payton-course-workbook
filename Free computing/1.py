d=list(map(int,['1','2','3','4','5','6',]))
print(d)

L = [ 2, 8, 12, -5, -10 ]
L3 = list(map((lambda t: t*2), L))
print("L3 = ", L3)


c=list(map(lambda t: t*2, [1,3,4,4]))
print(*c)


def calcs(a,b):
    return a+b
str1=['Ми']
v=list(map(len, str1))
print(v)

spis_lis=list(map(int,input('Введите цифы через пробел ').split()))
print(spis_lis)



x=list(map(lambda a,b:a+b,range(10),range(5)) )
print(x)