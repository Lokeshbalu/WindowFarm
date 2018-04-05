import socket
import threading
soc=socket.socket()
ip="192.168.43.49"
port=2010
port1=2000
port2=2020
motarstat=0
temp=0
hum=0
alarm=0
status=0
sack=0
soc=socket.socket()
soc1=socket.socket()
soc2=socket.socket()
soc.bind((ip,port))
soc1.bind((ip,port1))
soc2.bind((ip,port2))
soc.listen(10)
soc1.listen(10)
soc2.listen(10)
c,addr=soc.accept()
c2,addr=soc1.accept()
c3,addr=soc2.accept()
print(str(c))
print(str(c2))
print(str(c3))

def mobresponder(rport,sport):
	global sack
	global temp
	global hum
	global motarstat
	kk=rport.recv(1024)
	kk=kk.decode('utf-8')
	print(kk)
	if kk=="on":
		sack=1
		print("command on")
		sport.send("on".encode("utf-8"))
	if kk=="off":
		sack=2
		print("command off")
		sport.send("off".encode("utf-8"))
	if kk=="det":
		print("command det")
		l=str(motarstat)+"\r\n"+str(temp)+"\r\n"+str(hum)+"\r\n"
		print("stat"+"\r\n"+l)
		if motarstat==1:
			sport.send("on".encode('utf-8'))
		if motarstat==0:
			sport.send("off".encode('utf-8'))

hai=threading.Thread(target=mobresponder,args=(c2,c3))
hai.start()
while True:
	k=c.recv(1024)
	k=k.decode('utf-8')
	print(k)
	k=k.split("\r\n")
	if k[0]=="1":
		alarm=1
	if alarm==1 and status==0:
		c3.send("on".encode('utf-8'))
		alarm=0
		status=1
	if k[0]=="0":
		if status==1:
			alarm=0
			c3.send("off".encode('utf-8'))
		status=0
	temp=int(k[2])
	hum=int(k[3])
	if sack==0:
		c.send("ok".encode("utf-8"))
	if sack==1:
		c.send("on".encode("utf-8"))
		sack=0
	if sack==2:
		c.send("off".encode("utf-8"))
		sack=0
