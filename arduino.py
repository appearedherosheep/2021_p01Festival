import serial
import time


def arduino_input():
    ser = serial.Serial('COM8', 9600, timeout=1)
    while 1:
        if ser.readable():
            val = ser.readline()
            # print(val.decode()[:len(val)-1])
            # print(val.decode())
            val = val.decode()[:len(val)-1]
            # print(type(val))
            print(val)

            if len(val) > 0:
                print('Button CLicked')
                return 1


# arduino_input()
