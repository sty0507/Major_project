import serial

ser = serial.Serial(port="COM5", baudrate=9600)
ser.write("Hello world")
x = ser.readline()
print(x)