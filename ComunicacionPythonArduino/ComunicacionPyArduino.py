import sys
import time
import serial
import struct

serialPort1 = serial.Serial('COM15', timeout=None, baudrate=1000000)  # open serial port

#Give it a couple of seconds, sometimes seem to get connection issues.
print("initialising\n")
time.sleep(5)

#Big-endian >. Format i: integer -> 4bytes
# print("Big-endian")
# dataSerial = struct.pack('>iii',1,2,3)
# print("dataSerial: ", dataSerial)

#Little-endian >. Format i: integer -> 4 bytes
# print("Little-endian")
# dataSerial = struct.pack('<iii',1,2,3)
# print("dataSerial: ", dataSerial)
#
# #Big-endian >. Format B: unsigned char -> 1 byte
# print("Big-endian Format B")
# datoEmpaquetado = struct.pack('>BBB',1,2,3)
# print("dataSerial: ", datoEmpaquetado)

for vel in range(100,200,10):
#vel = 100
    print('velocidad: ',vel)
    array = [240,vel,vel,vel,247] #//240 o 0xF0 ; 247 o 0xF7
    datoEmpaquetado = struct.pack('>5B',*array)
    print("datoEmpaquetado",datoEmpaquetado)
    serialPort1.write(datoEmpaquetado)
    time.sleep(.5)
#time.sleep(1)
#data_raw = serialPort1.read(1)
#print("read: ",data_raw)
time.sleep(1)
serialPort1.close()
print(sys.byteorder)