import csv
from enum import Enum
from lib2to3.pgen2.grammar import line

import serial
import csv
import StringHelper as sth
import pandas as pd
import datetime

from StringHelper import *


class Controller:
    "TODO: Change the standard values of the __init__ method"

    def __init__(self, port="/dev/ttyACM0"):
        self._port = port
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = port  # If Using Linux
        # Specify the TimeOut in seconds, so that SerialPort
        # Doesn't hangs
        self.ser.timeout = 10
        self.ser.open()  # Opens SerialPort

        # print port open or closed
        if self.ser.isOpen():
            self.ser.write("udp open \r\n".encode('UTF-8'))
            self.ser.write(" udp bind :: {}\r\n".format(port).encode('UTF-8'))
            print("Open: ' + ser.portstr")

    def console(self):
        while 1:
            self.ser.reset_input_buffer()
            temp = input(" > ") + "\r\n"
            if "exit" in temp:
                break
            self.ser.write(temp.encode('UTF-8'))  # Writes to the SerialPort
            _line = self.ser.readline().decode('UTF-8')  # Read from Serial Port
            while 1:
                next_line = self.ser.readline().decode('UTF-8')  # Read from Serial Port
                if (_line == "> \r\n" and next_line == '> ') or next_line == _line:
                    break
                if not _line == "> \r\n":
                    print(_line, end="")  # Print What is Read from Port
                _line = next_line
        exit()

    def udp(self, ipaddr="ff03::1", payload="0", port="1212", file_name="results/result.csv"):
        self.ser.write("udp send {} {} {}\r\n".format(ipaddr,port, payload).encode('UTF-8'))
        try:
            _line = self.ser.readline().decode('UTF-8') # Read from Serial Port
        except Exception as e:
            print(e)
            return
        while 1:
            _next_line = self.ser.readline().decode('UTF-8') # Read from Serial Port
            if (_line == "> \r\n" and _next_line == '> ') or _next_line == _line:
                break
            if not _line == "> \r\n":
                print(_line, end="")  # Print What is Read from Port
                if file_name != "" and "bytes from " in _line:
                    append_line(file_name=file_name, line=_line)
                    return
            _line = _next_line


    def ping(self, ipaddr="ff03::1", size=12, count=1, interval=1, file_name="results/result.csv"):
        "TODO: Error 5: Busy try to wait longer DOKUMENTIEREN"
        "https://github.com/openthread/openthread/blob/master/src/cli/README.md#ping-ipaddr-size-count-interval-hoplimit"
        interval = round(interval, 5)
        self.ser.write("ping {} {} {} {} \r\n".format(ipaddr, size, count, interval).encode('UTF-8'))
        try:
            _line = self.ser.readline().decode('UTF-8') # Read from Serial Port
        except Exception as e:
            print(e)
            return
        while 1:
            _next_line = self.ser.readline().decode('UTF-8') # Read from Serial Port
            if "Error 5: Busy" in _line:
                _next_line = self.ser.readline().decode('UTF-8')
                self.ser.write("ping {} {} {} {} \r\n".format(ipaddr, size, count, interval).encode('UTF-8'))
            if (_line == "> \r\n" and _next_line == '> ') or _next_line == _line:
                break
            if not _line == "> \r\n":
                print(_line, end="")  # Print What is Read from Port
                if file_name != "":
                    append_line(file_name=file_name, line=_line, interval=interval)
            _line = _next_line

    def get_any_ip(self):
        try:
            os.remove("results/result.csv")
        except Exception:
            print("File doesnt exist... Starting Test")
        self.ping()
        results = pd.read_csv("results/result.csv",
                              usecols=[sth.PingValues.IPADDR.value])
        return results.values[0][0]
