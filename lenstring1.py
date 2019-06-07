c=input()
c=int(c)
K=[]
for i in range(0,c):  
    y=input()
    K.append(y)
R=[]
for i in zip(*K):
    if i.count(i[0])==len(i): 
        R.append(i[0])
    else:
        break
print(''.join(R))
