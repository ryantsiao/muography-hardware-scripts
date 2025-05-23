import serial
import time

ser = serial.Serial("/dev/serial0",115200,timeout=1)

print("started reading TFmini")
while True:
    print(ser.in_waiting)
    if ser.in_waiting>=9:
        data=ser.read(9)
        if data[0]==0x59 and data[1]==0x59:
            distance=data[2]+data[3]*256
            strength=data[4]+data[5]*256
            print("Distance:{} cm, Strength: {}".format(distance,strength))
    time.sleep(0.1)
            
