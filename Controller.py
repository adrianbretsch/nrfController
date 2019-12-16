import serial

# Global Variables
ser = 0


# Function to Initialize the Serial Port
def init_serial(port) -> serial:
    global ser  # Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = port  # If Using Linux
    # Specify the TimeOut in seconds, so that SerialPort
    # Doesn't hangs
    ser.timeout = 1
    ser.open()  # Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print("Open: ' + ser.portstr")
    return ser


def console(__ser: serial.Serial):
    while 1:
        __ser.reset_input_buffer()
        temp = input(" > ") + "\r\n"
        if "exit" in temp:
            break
        __ser.write(temp.encode('ascii'))  # Writes to the SerialPort
        line = __ser.readline().decode('ascii')  # Read from Serial Port
        while 1:
            next_line = __ser.readline().decode('ascii')  # Read from Serial Port
            if (line == "> \r\n" and next_line == '> ') or next_line == line:
                break
            if not line == "> \r\n":
                print('nRF: ' + line, end="")  # Print What is Read from Port
            line = next_line
    exit()


def ping_all(__ser: serial.Serial):
    __ser.reset_input_buffer()
    __ser.write("\r\n ping ff03::1".encode('ascii'))
    line = __ser.readline().decode('ascii')
    while 1:
        next_line = __ser.readline().decode('ascii')  # Read from Serial Port
        if (line == "> \r\n" and next_line == '> ') or next_line == line:
            break
        if not line == "> \r\n":
            print('ping: ' + line, end="")  # Print What is Read from Port
            line = next_line
