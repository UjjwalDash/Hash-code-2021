N=list(map(int,input().split()))
P=[['onion', 'pepper', 'olive'], ['chicken', 'mushroom', 'pepper'],
   ['mushroom', 'tomato', 'basil'],['tomato', 'mushroom', 'basil'],
   ['chicken', 'basil']]
#p=P[0]+P[1]+P[2]+P[3]+P[4]
A=[]
M=N[0]
T2=N[1]
T3=N[2]
T4=N[3]
c=0
for l in range(0,M):
    I=list(map(str,input().split()))
    I.remove(I[0])
    A.append(I)
#for team A2
p=[]
p1=[]
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        I1=A[i]+A[j]
        a=set(I1)
        #p.append([i,j,len(a)])
        if (len(a)*len(a)==16):
            print(2,i,j)
            c=c+1
            A[i]=[]
            A[j]=[]
            #break
    #if c==T2:
        #break
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            I1=A[i]+A[j]+A[k]
            a=set(I1)
            #p1.append([i,j,len(a)])
            if (len(a)*len(a)==49):
                print(2,i,j,k)
                c=c+1
                A[i]=[]
                A[j]=[]
                #break
    #if c==T2:
        #break
        
  
'''5 1 2 1
3 onion pepper olive
3 mushroom tomato basil
3 chicken mushroom pepper
3 tomato mushroom basil
2 chicken basil'''
