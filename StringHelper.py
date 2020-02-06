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
    INTERVAL = 'interval'
    ERROR = 'error'


class UdpValues(Enum):
    BYTES = 'bytes'
    IPADDR = 'ipaddr'
    PORT = 'port'
    MESSAGE = 'message'
    TIME = 'time'
    ERROR = 'error'


def append_line(file_name="", line="", interval="", time="") -> dict:
    if not file_name == "" and "icmp" in line and not "ping" in line:
        ping_dic = _parse_ping(line, interval)
        _append_row(file_name, ipaddr=ping_dic.get(PingValues.IPADDR),
                    package_bytes=ping_dic.get(PingValues.BYTES),
                    icmp_seq=ping_dic.get(PingValues.ICMP_SEQ),
                    hlim=ping_dic.get(PingValues.HLIM),
                    time=ping_dic.get(PingValues.TIME),
                    interval=ping_dic.get(PingValues.INTERVAL),
                    error=ping_dic.get(PingValues.ERROR))
        return ping_dic
    elif not file_name == "" and "bytes from" in line:
        udp_dic = _parse_udp(line)
        _append_row(file_name,
                    package_bytes=udp_dic.get(UdpValues.BYTES),
                    ipaddr=udp_dic.get(UdpValues.IPADDR),
                    port=udp_dic.get(UdpValues.PORT),
                    message=udp_dic.get(UdpValues.MESSAGE),
                    time=time,
                    error=udp_dic.get(UdpValues.ERROR))
        return udp_dic


def _parse_udp(line) -> dict:
    line = line.replace("bytes from ", "").replace("> ", "").replace("\r\n", "")
    values = line.split(" ")
    udp_values = dict()
    try:
        udp_values = dict({UdpValues.BYTES: values[0],
                           UdpValues.IPADDR: values[1],
                           UdpValues.PORT: values[2],
                           UdpValues.MESSAGE: values[3],
                           UdpValues.ERROR: ""
                           })
    except Exception:
        print("[ERROR]: " + line)
    if "Error" in line:
        udp_values = dict({UdpValues.BYTES: "",
                           UdpValues.IPADDR: "",
                           UdpValues.PORT: "",
                           UdpValues.MESSAGE: "",
                           UdpValues.ERROR: line
                           })
    return udp_values;


def _append_row(file_name, ipaddr="", package_bytes="", icmp_seq="", hlim="", time="", interval="", port="", message="",
                error=""):
    exists = os.path.isfile(file_name)
    with open(file_name, 'a') as file:
        fieldnames = []
        if not icmp_seq == "":
            for value in PingValues:
                fieldnames.append(value.value)
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not exists:
                writer.writeheader()
            writer.writerow({PingValues.BYTES.value: package_bytes, PingValues.IPADDR.value: ipaddr,
                             PingValues.ICMP_SEQ.value: icmp_seq, PingValues.HLIM.value: hlim,
                             PingValues.TIME.value: time, PingValues.INTERVAL.value: interval,
                             PingValues.ERROR.value: error})
        elif ipaddr != "":
            for value in UdpValues:
                fieldnames.append(value.value)
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not exists:
                writer.writeheader()
            writer.writerow({UdpValues.BYTES.value: package_bytes, UdpValues.IPADDR.value: ipaddr,
                             UdpValues.PORT.value: port, UdpValues.MESSAGE.value: message, UdpValues.TIME.value: time, UdpValues.ERROR.ERROR.value:error
                             })


def _parse_ping(line="", interval="") -> dict:
    line = line.replace("bytes from ", "").replace("> ", "").replace("\r\n", "")
    values = line.split(" ")
    ping_values = dict()
    try:
        ping_values = dict({PingValues.BYTES: values[0],
                            PingValues.IPADDR: values[1][:-1],
                            PingValues.ICMP_SEQ: values[2].replace("icmp_seq=", ""),
                            PingValues.HLIM: values[3].replace("hlim=", ""),
                            PingValues.TIME: "0",
                            PingValues.INTERVAL: interval,
                            PingValues.ERROR: ""})
        if "time" in line:
            ping_values[PingValues.TIME] = values[4].replace("time=", "").replace("ms", "")

    except Exception:
        print("[ERROR]: " + line)
    if "Error" in line:
        ping_values = dict({PingValues.BYTES: "",
                            PingValues.IPADDR: "",
                            PingValues.ICMP_SEQ: "",
                            PingValues.HLIM: "",
                            PingValues.TIME: "",
                            PingValues.INTERVAL: interval,
                            PingValues.ERROR: line})
    return ping_values
