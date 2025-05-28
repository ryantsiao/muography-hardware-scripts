import serial
import time
from datetime import datetime

with open("/home/arratialab/Lidar_logs/Log_{}.txt".format(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")),"w") as f:
  start = time.time()
  ser = serial.Serial("/dev/serial0",115200,timeout=1)

  print("started reading TFmini")
  while True:
      print(ser.in_waiting)
      if ser.in_waiting>=9:
          line1 = datetime.now().strftime("%H:%M:%S")
          print(line1)
          f.write("{}|".format(line1))
          data=ser.read(9)
          if data[0]==0x59 and data[1]==0x59:
              distance=data[2]+data[3]*256
              strength=data[4]+data[5]*256
              line2 = "Distance:{} cm|Strength: {}".format(distance,strength)
              print(line2)
              f.write("{}\n".format(line2))
      time.sleep(0.01)
