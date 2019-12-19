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


def append_row(file_name="", ipaddr="", package_bytes="", icmp_seq="", hlim="", time=""):
    if not file_name == "":
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
                             PingValues.TIME.value: time})
            print(file)


def parse_row(row: str) -> list:
    return []
