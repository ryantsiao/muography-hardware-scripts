# LIDAR Script

This folder contains code to interface a raspberry pi with the TFmini LiDAR sensor via UART.

## Hardware connections

- Connect sensor wires to raspberry pi pins via female-female jumper wires
  - More information on wire connections can found in the [TFmini manual](https://github.com/TFmini/TFmini-Plus/blob/master/SJ-PM-TFmini%20Plus%20A04%20Product%20Manual.pdf) and online diagrams for the raspberry pi
  - Ensure sensor's RX pin is connected to pi's TX pin, and vice versa
## Software Setup

- Enable Serial Port on raspberry pi
  - Enter sudo rapi-config into command line
  - Go to interface options and then serial port
  - Do not login shell over serial, but enable serial port hardware
  - Exit and reboot
- If pyserial is not installed on raspberry pi, install it using sudo apt install

- It should now be connected, run test_lidar.py to test

