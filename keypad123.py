import RPi.GPIO as io
import time
from time import sleep
io.setwarnings(False)

io.setmode(io.BOARD)

password="1231"
count=0
c1=3
c2=5
c3=7
r0=8
r1=10
r2=11
r3=12
b=""

io.setup(c1,io.IN,io.PUD_UP)
io.setup(c2,io.IN,io.PUD_UP)
io.setup(c3,io.IN,io.PUD_UP)
io.setup(r0,io.OUT)
io.setup(r1,io.OUT)
io.setup(r2,io.OUT)
io.setup(r3,io.OUT)

#io.setup(c1,io.HIGH)

#io.setup(c2,io.HIGH)
#io.setup(c3,io.HIGH)



def readKey():
	io.output(r0,0)
	io.output(r1,1)
	io.output(r2,1)
        io.output(r3,1)
        if(io.input(c1)==0):
		sleep(0.5)
        	return'1'
        if(io.input(c2)==0):
                sleep(0.5)
                return'2'
        if(io.input(c3)==0):
                sleep(0.5)
                return'3'
        return'o'

def  nfun():
	key='o'
	while(key=='o'):
	        key=readKey()
        
	return key

while(count<4):

	a=nfun()
	b=b+a
	count+=1

print b

if(b==password):
	print("password unlocked")

else :
	print("wrong password")
