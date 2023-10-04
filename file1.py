L=[]
n=int(input("Enter Limit:"))

for i in range(n):
        x=int(input("Enter input:"))
        L=L+[x]
print(L)
for i in range(n):
        if(L[i]%2==0):
            L[i]=L[i]+1
        else:
            L[i]=L[i]+2

print(L)
