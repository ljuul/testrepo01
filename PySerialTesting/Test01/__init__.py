import sys
import serial
#from PyQt4 import QtGui



ser = serial.Serial(4) #connect to serial port
print ser.portstr #print port name e.g., COM5
print ser.inWaiting()
raw_input("Press Enter to continue...")

if ser.inWaiting()>0:
    ser.flush() #flush receive buffer
#
ser.write("++mode 1\n") #GPIB dongle is CONTROLLER ("all your base are belong to us")
ser.write("++addr 20\n") #VNA address is set to 20
ser.write("++auto 1\n") #TALK goddammit, VNA!
#
#ser.write("++eoi 1\n") #enable use of EOI signal with last char of every cmd
#ser.write("++eos 0\n") #append CR-LF to host commands
ser.write("++eot_enable 1\n") #I want to see when the VNA sends and EOI signal
ser.write("++eot_char 4\n") #And that signal must be ascii character 4 (EOT - end of transmission) 
#
#ser.write("MMEM:CAT?\n")
#ser.write("TRAC? CH1DATA")
#line=ser.readline()
#print line
ser.write("MMEM:CDIR 'C:\R_S\INSTR\Temp'\n") #change VNA directory
#ser.write("MMEM:CDIR 'C:\USER\CONFIG'\n") #change VNA directory
#ser.write("MMEM:CAT?\n")
#line=ser.readline()
#print line
"""
app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(250, 150)
w.move(300, 300)
w.setWindowTitle('Simple')
w.show()
    
sys.exit(app.exec_())

"""

try:
    with open('spool.wmf', 'wb') as f: 
        ser.write("MMEM:DATA? 'spool.wmf'\n") #access file on VNA
        inchar = 0

        print ser.inWaiting()
        raw_input("Press Enter to continue...")

        
        while ser.inWaiting()>0:
            inchar = ord(ser.read())
            sys.stdout.write(chr(inchar))
            f.write(chr(inchar))
        
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)

finally:
    f.close()#close file
    print "\nFile closed"
     
ser.write("++loc\n") #return to operation of VNA control panel
ser.close() #close connection to serial port
