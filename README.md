# miscellaneous

## Raspberry Pi UART Tests
Enable UART ports on the Raspberry Pi by adding these lines to /boot/config.txt:
- enable_uart=1
- dtoverlay=uart2
- dtoverlay=uart4

Load the serial reader project onto an Arduino (must have multiple serial ports, so don't use an uno) and connect RX on the Pi to TX1 on the Arduino and TX on the Pi to RX1 on the Arduino. Ground the Pi and the Arduino together.

Run the python script on the Raspberry Pi in supervisor mode (use sudo).
