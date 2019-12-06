
import serial

# Can be Downloaded from this Link
# https://pypi.python.org/pypi/pyserial

# Global Variables
ser = 0


# Function to Initialize the Serial Port
def init_serial():
    global ser  # Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM1' #If Using Linux

    # Specify the TimeOut in seconds, so that SerialPort
    # Doesn't hangs
    ser.timeout = 10
    ser.open()  # Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print("Open: ' + ser.portstr")

# Function Ends Here


# Call the Serial Initilization Function, Main Program Starts from here
init_serial()
#ser.write("\r\n".encode("ascii"))
while 1:
    ser.reset_input_buffer()
    temp = input(" > ") + "\r\n"
    if "exit" in temp:
        break
    ser.write(temp.encode('ascii'))  # Writes to the SerialPort
    while 1:
        line = ser.readline().decode('ascii')  # Read from Serial Port
        if line == "> \r\n" or "Error" in line:
            break
        print ('nRF: ' + line)# Print What is Read from Port

exit()
# Ctrl+C to Close Python Window

