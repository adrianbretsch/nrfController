import csv

import serial
import pandas as pd


# Global Variables

def parse_to(row):
    t = open('employee_file2.csv', 'a')
    with t as file:
        file.write(row)
        print(file)


class Controller:
    def __init__(self, port):
        self._port = port
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = port  # If Using Linux
        # Specify the TimeOut in seconds, so that SerialPort
        # Doesn't hangs
        self.ser.timeout = 1
        self.ser.open()  # Opens SerialPort

        # print port open or closed
        if self.ser.isOpen():
            print("Open: ' + ser.portstr")

    def console(self):
        while 1:
            self.ser.reset_input_buffer()
            temp = input(" > ") + "\r\n"
            if "exit" in temp:
                break
            self.ser.write(temp.encode('ascii'))  # Writes to the SerialPort
            line = self.ser.readline().decode('ascii')  # Read from Serial Port
            while 1:
                next_line = self.ser.readline().decode('ascii')  # Read from Serial Port
                if (line == "> \r\n" and next_line == '> ') or next_line == line:
                    break
                if not line == "> \r\n":
                    print(line, end="")  # Print What is Read from Port
                line = next_line
        exit()

    def ping_all(self, ):
        self.ser.reset_input_buffer()
        self.ser.write("\r\n ping ff03::1 \r\n".encode('ascii'))
        lines = self.ser.readall().decode('ascii')
        for line in lines:
            line = line.strip()
            print(line)

        """
        while 1:
            next_line = self.ser.readline().decode('ascii')  # Read from Serial Port
            if (line == "> \r\n" and next_line == '> ') or next_line == line:
                break
            if not line == "> \r\n":
                print(line, end="")  # Print What is Read from Port
            line = next_line
        """

    def ping(self, ipaddr, size, count, interval, hoplimit):
        self.ser.reset_input_buffer()

        self.ser.write("ping {} {} {} {} {}".format(ipaddr, size, count, interval, hoplimit).encode('ascii'))
        line = self.ser.readline().decode('ascii')  # Read from Serial Port
        while 1:

            next_line = self.ser.readline().decode('ascii')  # Read from Serial Port
            if (line == "> \r\n" and next_line == '> ') or next_line == line:
                break
            if not line == "> \r\n":
                print(line, end="")  # Print What is Read from Port
                parse_to()
            line = next_line
