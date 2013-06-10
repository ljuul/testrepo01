from serial.tools import list_ports
import serial
import os

def list_serial_ports():
    # Windows
    if os.name == 'nt':
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append('COM'+str(i + 1))
                s.close()
            except serial.SerialException:
                pass
        return available
    else:
        # Mac / Linux
        return [port[0] for port in list_ports.comports()]

def main():
    available=list_serial_ports()
    print(available)
    
"""
print ser.portstr

ser.write("++read eoi\n")



ser.write("MMEM:CDIR 'C:\'\n") #change VNA directory
ser.write("MMEM:CAT?\n")
line=ser.readline()
print line

ser.write("++loc\n")
ser.close()
"""
