n,k=map(int,input().split())
m=100001;v=[m]*m;v[n]=0;q=[n];c=1
while q:
 x=q.pop(0)
 for i in(x-1,x+1,x*2):
  if 0<=i<m and v[x]+1<=v[i]:
   if v[k]==m:v[i]=v[x]+1;q.append(i)
   elif i==k:c+=1
print(v[k])
print(c)