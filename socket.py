
a = open('Perepis.txt')
f = a.read()
d=f.split('\n')
i=int(0)
c=int(0)
while(d[i]!=''):
    p=d[i].split()

    g=p[3].split('.')

    t=int(g[2])
    if(t<=1978):
        print(p[0])
        c=c+1
    i=i+1
print(c)
i=0
x=int(input())
y=int(input())

while(d[i]!=''):
    p=d[i].split()
    g=p[3].split('.')
    t=int(g[2])
    if(t<=y)and(t>=x):
        print(p[0])
    i=i+1

a.close()

