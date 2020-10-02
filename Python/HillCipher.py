from array import *



mess=input("Enter the message")
ke=input("Enter the key")
message=[]
key=[][]

message_length=len(message)
length=message_length*message_length
k=0

for i in range(len(ke),length):
    ke+=ke[k]
    k=k+1

k=0
for i in range(0,message_length) :
    for j in range(0,message_length):
        key[i][j]=ke[k]

k=0
for i in range(0,message_length) :
    for j in range(0,1):
        message[i][j]=mess[k]

def encrypt(message, key):


encrypt(message,key)
