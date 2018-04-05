import machine
import socket
import time
import network
import dht
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
time.sleep(2)
while not sta_if.isconnected():
	sta_if.connect("new","RVLBlokesh")
pin4=machine.Pin(4,machine.Pin.OUT)
sens=dht.DHT11(machine.Pin(2))
ip="192.168.43.49"
port=2010
soc=socket.socket()
pin0=machine.ADC(0)
thres=600
time.sleep(9)
motarStat=0
soc.connect((ip,port))
sens.measure()
while True:
	temp=sens.temperature()
	hum=sens.humidity()
	k=pin0.read()
	print(k)
	if k>900:
		pin4.on()
		motarStat=1
	if k<600:
		pin4.off()
		motarStat=0
	l=str(motarStat)+"\r\n"+str(k)+"\r\n"+str(temp)+"\r\n"+str(hum)
	soc.send(l.encode('utf-8'))
	rec=soc.recv(1024)
	rec=rec.decode('utf-8')
	if rec=="ok":
		pass
	if rec=="on":
		pin4.on()
		motarStat=1
	if rec=="off":
		pin4.off()
		motarStat=0
