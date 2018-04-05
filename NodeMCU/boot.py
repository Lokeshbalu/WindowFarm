#this file is executed on every boot
#import esp
#esp.osdebug(None)
import gc
import network
#import webrepl
#webrepl.start()
gc.collect()
#pyb.main('main.py') # main script to run after this one
#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
#Network associated code
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
while not sta_if.isconnected():
	sta_if.connect("new","RVLBlokesh")

