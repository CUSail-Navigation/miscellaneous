import serial
import time

# UART 1: GPIO RX:15, TX:14
#serial_port = serial.Serial(port='/dev/serial0', baudrate=9600, timeout=5)

# UART 2: GPIO RX:1, TX:0
#serial_port = serial.Serial(port='/dev/ttyAMA1', baudrate=9600, timeout=5)

# UART 4: GPIO RX:9, TX:8
serial_port = serial.Serial(port='/dev/ttyAMA2', baudrate=9600, timeout=5)


for i in range(20):
    msg = 'test ' + str(i) + '\n'
    serial_port.write(msg.encode('utf-8'))
    serial_port.flush()
    time.sleep(1)
    