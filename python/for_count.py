
m=0
n=int(input("숫자 입력해"))
for i in range(n+1):
    k=i%2
    if(k==0):
        m=m+i

print(m)