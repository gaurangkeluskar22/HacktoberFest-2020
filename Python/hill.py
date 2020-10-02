#Encryption
def check(i):
    n=int(0)
    if i.isupper():
        v=ord(i)-65
        n=65
    elif i.islower():
        v=ord(i)-97
        n=97
    else:
        v=int(i)
    return v,n

def mtrxMul(mtrx1,mtrx2):
    cipherMtrx=[]
    for i in range(len(mtrx2)):
        sum=int(0)
        for j in range(len(mtrx2[i])):
            sum+=mtrx2[i][j]*mtrx1[j]
        sum=sum%26
        cipherMtrx.append(sum)
    return cipherMtrx

def mMtrx(m):
    mtrx=[]
    lst=[]
    for i in m:
        v,n=check(i)
        mtrx.append(v)
        lst.append(n)
    return mtrx,lst

def kMtrx(k,l):
    mtrx=[]
    for i in range(len(k)):
        v,n=check(k[i])
        if i%l==0:
            t=[]
            mtrx.append(t)
        t.append(v)
    return mtrx

def encrypt(message,key):
    cipher=""
    mtrx1,lst=mMtrx(message)
    mtrx2=kMtrx(key,len(message))
    cipherMtrx=mtrxMul(mtrx1,mtrx2)
    for i in range(len(cipherMtrx)):
        cipher+=chr(cipherMtrx[i]+lst[i])
    return cipher

message=input("Enter the message:")
key=input("Enter the key:")

def requiredKey(key,l):
    copy=key
    while(len(key)<=l*l):
        key+=copy
    return key[0:l*l]

key=requiredKey(key,len(message))
print("Cipher:",encrypt(message,key))

#Decryption
def transpose(mtrx,copy):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            copy[i][j]=mtrx[j][i]
    return copy

def determinant(mtrx):
    if len(mtrx)==1:
        d=mtrx[0][0]
        return d
    elif len(mtrx)==2:
        d=mtrx[0][0]*mtrx[1][1]-mtrx[0][1]*mtrx[1][0]
        return d
    else:
        eqn=int(0)
        for i in range(len(mtrx)):
            cof=[]
            for j in range(1,len(mtrx)):
                           e=[]
                           cof.append(e)
                           for k in range(len(mtrx[j])):
                               if k==i:
                                   continue
                               cof[j-1].append(mtrx[j][k])
            if i%2==0:
                s=1
                eqn+=mtrx[0][i]*determinant(cof)
            else:
                s=-1
                eqn-=mtrx[0][i]*determinant(cof)
        return eqn

def traverse(mtrx,a,b):
    c=[]
    k=int(-1)
    for i in range(len(mtrx)):
        if i==a:
            continue
            k=k-1
        t=[]
        c.append(t)
        k=k+1
        for j in range(len(mtrx[i])):
            if j==b:
                continue
            c[k].append(mtrx[i][j])
    d=determinant(c)
    return d

def adjoint(mtrx):
    l=len(mtrx)
    lst=[]
    copy="0"*(l**2)
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if (i+j)%2==0:
                s=1
            else:
                s=-1
            lst.append(str(s*traverse(mtrx,i,j)))
    transp=kMtrx(lst,l)
    copy=kMtrx(copy,l)
    adj=transpose(transp,copy)
    return adj

def decrypt(cipher,key):
    message=""
    mtrx1,lst=mMtrx(cipher)
    l=len(mtrx1)
    mtrx2=kMtrx(key,l)
    d=determinant(mtrx2)
    if d==0:
        print("Inverse of a matrix is not possible for decryption")
        print("Choose key such that inverse is possible")
    else:
        adjmtrx=adjoint(mtrx2)
        def getCoeff(a):
                for i in range(1,26):
                        j=int(1)
                        eqn=int(1)
                        while(eqn>=1):
                                eqn=26*i-a*j
                                if eqn==1:
                                        return -j
                                j=j+1
        d=getCoeff(d%26)
        if d is None:
            print("Decryption not possible")
            print("Choose a key such that its matrix determinant is prime")
        else:
            l=len(adjmtrx)
            invrsmtrx="0"*(l*l)
            invrsmtrx=kMtrx(invrsmtrx,l)
            for i in range(len(adjmtrx)):
                for j in range(len(adjmtrx[i])):
                    invrsmtrx[i][j]=adjmtrx[i][j]*d%26
            mssgmtrx=mtrxMul(mtrx1,invrsmtrx)
            for i in range(len(mssgmtrx)):
                message+=chr(mssgmtrx[i]+lst[i])
            return message

cipher=input("Enter the cipher:")
key=input("Enter the key:")

key=requiredKey(key,len(cipher))
print("Message:",decrypt(cipher,key))

