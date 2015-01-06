import os
import serial
from time import sleep

if not os.path.exists('/tmp/mklkfifo'):
    os.system('mkfifo /tmp/mklkfifo')

f = file('/tmp/mklkfifo','r')

ser = serial.Serial(4,9600)

def main():
    while 1:
        xp = f.read()
        if xp:
            ser.write(xp)
            ser.flushinput()
            
        uz = ser.inwaiting()
        if uz:
            nwrs = ser.read(uz)
            print nwrs
        sleep(0.1)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
            f.close()
            

        


