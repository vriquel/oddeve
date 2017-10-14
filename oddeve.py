l=[]
a=int(input("Enter a no"))
print("please enter",a,'these many nos in list')
i=0
while i<a:
    q=int(input())
    l.append(q)
    i+=1
for j in range(a+1):
    if j%2==1:
        print("Te no is odd")
        print(j)
#python program
