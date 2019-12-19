import csv
from enum import Enum
from lib2to3.pgen2.grammar import line

import serial
import csv
import pandas as pd
import datetime

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

    def ping(self, ipaddr="ff03::1", size=8, count=1, interval=1, file_name="results/result.csv"):
        self.ser.reset_input_buffer()
        "https://github.com/openthread/openthread/blob/master/src/cli/README.md#ping-ipaddr-size-count-interval-hoplimit"
        self.ser.write("ping {} {} {} {} \r\n".format(ipaddr, size, count, interval).encode('ascii'))
        _line = self.ser.readline().decode('ascii')  # Read from Serial Port
        while 1:
            _next_line = self.ser.readline().decode('ascii')  # Read from Serial Port
            if (_line == "> \r\n" and _next_line == '> ') or _next_line == _line:
                break
            if not _line == "> \r\n":
                print(_line, end="")  # Print What is Read from Port
                append_line(file_name=file_name, line=_line)
            _line = _next_line
