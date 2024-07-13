from AP33772 import *
#import machine
#i2c    = machine.I2C(1,sda=machine.Pin(6), scl=machine.Pin(7), freq=400000) #xiao rp2040
#en_pin = machine.Pin(3, machine.Pin.OUT) # en_pin connects to 3V3 pin on mikroe click board
import smbus
i2c = smbus.SMBus(1) # raspberry pi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) # USE RPi GPIO 4, next to I2C pins, connect to 3V3 pin on mikroe click board

#en_pin.value(1)
GPIO.output(4, GPIO.HIGH)

USB_PD = AP37772(i2c=i2c)
for pdo_num in range(1,8):
    USB_PD.get_pdo(pdo_num)
USB_PD.get_pdo_num()
USB_PD.get_voltage()
USB_PD.get_current()
USB_PD.get_temp()
USB_PD.send_rdo(type='FIXED', pdo_num=1, op_current=2.8, max_current=3.0)
USB_PD.get_pdo_status()
USB_PD.send_rdo(type='PPS', pdo_num=6, op_current=3.0, voltage=8.2)
USB_PD.send_rdo_reset()

#en_pin.value(0)
GPIO.output(4, GPIO.LOW)
