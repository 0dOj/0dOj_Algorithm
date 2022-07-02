n,a,b=map(int, input().split());c=0
while a!=b:c+=1;a-=a//2;b-=b//2
print(c)