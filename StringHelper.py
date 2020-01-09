# Global Variables
import csv
from enum import Enum
import os.path


class PingValues(Enum):
    BYTES = 'bytes'
    IPADDR = 'ipaddr'
    ICMP_SEQ = 'icmp_seq'
    HLIM = 'hlim'
    TIME = 'time'
    ERROR = 'error'


def append_line(file_name="", line=""):
    if not file_name == "" and not "ping" in line:
        ping_dic = _parse_ping(line)
        _append_row(file_name, ipaddr=ping_dic.get(PingValues.IPADDR),
                    package_bytes=ping_dic.get(PingValues.BYTES),
                    icmp_seq=ping_dic.get(PingValues.ICMP_SEQ),
                    hlim=ping_dic.get(PingValues.HLIM),
                    time=ping_dic.get(PingValues.TIME),
                    error=ping_dic.get(PingValues.ERROR))


def _append_row(file_name, ipaddr="", package_bytes="", icmp_seq="", hlim="", time="", error=""):
    exists = os.path.isfile(file_name)
    with open(file_name, 'a') as file:
        fieldnames = []
        for value in PingValues:
            fieldnames.append(value.value)
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow({PingValues.BYTES.value: package_bytes, PingValues.IPADDR.value: ipaddr,
                         PingValues.ICMP_SEQ.value: icmp_seq, PingValues.HLIM.value: hlim,
                         PingValues.TIME.value: time, PingValues.ERROR.value: error})


def _parse_ping(line="") -> dict:
    line = line.replace("bytes from ", "").replace("> ", "").replace("\r\n", "")
    values = line.split(" ")
    ping_values = dict()
    try:
        ping_values = dict({PingValues.BYTES: values[0],
                            PingValues.IPADDR: values[1][:-1],
                            PingValues.ICMP_SEQ: values[2].replace("icmp_seq=", ""),
                            PingValues.HLIM: values[3].replace("hlim=", ""),
                            PingValues.TIME: "0",
                            PingValues.ERROR: ""})
        if "time" in line:
            dict[PingValues.TIME] = values[4].replace("time=", "").replace("ms", "")
        if "Error" in line:
            print("ERROR in Line: " + line)
            ping_values = dict({PingValues.BYTES: "",
                                PingValues.IPADDR: "",
                                PingValues.ICMP_SEQ: "",
                                PingValues.HLIM: "",
                                PingValues.TIME: "",
                                PingValues.ERROR: line})
    except Exception:
        print("ERROR in Line: " + line)
    return ping_values
