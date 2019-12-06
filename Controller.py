
import serial

# Can be Downloaded from this Link
# https://pypi.python.org/pypi/pyserial

# Global Variables
ser = 0


# Function to Initialize the Serial Port
def _init_serial():
    global ser  # Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM1' #If Using Linux

    # Specify the TimeOut in seconds, so that SerialPort
    # Doesn't hangs
    ser.timeout = 1
    ser.open()  # Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print("Open: ' + ser.portstr")

def console():
    _init_serial()
    while 1:
        ser.reset_input_buffer()
        temp = input(" > ") + "\r\n"
        if "exit" in temp:
            break
        ser.write(temp.encode('ascii'))  # Writes to the SerialPort
        line = ser.readline().decode('ascii')  # Read from Serial Port
        while 1:
            next_line = ser.readline().decode('ascii')  # Read from Serial Port
            if (line == "> \r\n" and next_line == '> ') or next_line == line:
                break
            if not line == "> \r\n":
                print('nRF: ' + line, end="")# Print What is Read from Port
            line = next_line
    exit()
