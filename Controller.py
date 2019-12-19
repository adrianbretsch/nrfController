import csv
from enum import Enum

import serial
import csv
import pandas as pd

from StringHelper import *


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

    def ping(self, file_name="result.txt", ipaddr="ff03::1", size=8, count=1, interval=1):
        self.ser.reset_input_buffer()
        "https: // github.com / openthread / openthread / blob / master / src / cli / README.md  # ping-ipaddr-size-count-interval-hoplimit"
        self.ser.write("ping {} {} {} {} \r\n".format(ipaddr, size, count, interval).encode('ascii'))
        line = self.ser.readline().decode('ascii')  # Read from Serial Port
        with open(file_name, 'w') as file:
            file.write("")
        while 1:
            next_line = self.ser.readline().decode('ascii')  # Read from Serial Port
            if (line == "> \r\n" and next_line == '> ') or next_line == line:
                break
            if not line == "> \r\n":
                with open(file_name, 'a') as file:
                    file.write(line)
                print(line, end="")  # Print What is Read from Port
            line = next_line


