import datetime

import Controller
import StringHelper as sth
import os
import numpy
import pandas as pd
import itertools


def init(test_name, size=0, interval=0, count=0, hops=-1):
    now = datetime.datetime.now()
    file_name = test_name
    if not size == 0:
        file_name = "{}_s-{}".format(file_name, size)
    if not interval == 0:
        file_name = "{}_i-{}".format(file_name, interval)
    if not count == 0:
        file_name = "{}_c-{}".format(file_name, count)
    if not hops == -1:
        file_name = "{}_h-{}".format(file_name, hops)
    file_name = "{}_{}.csv".format(file_name, now.strftime("%x_%X").replace(":", "-").replace("/", "-"))
    file_path = os.path.join("results", test_name, file_name)
    try:
        # Create target Directory
        os.mkdir("results")
        print("Directory results Created ")
    except FileExistsError:
        print("Directory results --> OK")
    try:
        # Create target Directory
        os.mkdir("results/" + test_name)
        print("Directory ", test_name, " Created ")
    except FileExistsError:
        print("Directory ", test_name, " --> OK")
    return file_path


def multicast_package_test():
    "Tests the reliability of the network based on the package size of a multicast"
    test_name = "multicast-package-test"
    file_path = init(test_name)
    for size in range(202, 992, 10):
        controller.ping(size=size, count=10, interval=10, file_name=file_path)


def multicast_interval_test():
    test_name = "multicast-interval-test"
    "smallest 0.001"
    for interval in numpy.arange(0.5, 0.0009, -0.01):
        file_path = init(test_name=test_name, interval=interval)
        controller.ping(size=12, count=20, interval=interval, file_name=file_path)


def multicast_stability_test():
    test_name = "multicast-stability-test"
    while 1:
        file_path = init(test_name=test_name)
        controller.ping(size=2, count=604800, file_name=file_path)


def unicast_package_test():
    "Tests the reliability of the network based on the package size of a multicast"
    test_name = "unicast_package_test"
    ip_address = controller.get_any_ip()
    file_path = init(test_name)
    for size in range(12, 992, 10):
        controller.ping(ipaddr=ip_address, size=size, count=20, interval=5, file_name=file_path)


def unicast_interval_test():
    test_name = "unicast_interval_test"
    count = 20
    "smallest 0.001"
    ip_address = controller.get_any_ip()

    file_path = init(test_name=test_name)
    for interval in numpy.arange(0.05, 0.0009, -0.001):
        controller.ping(ipaddr=ip_address, size=12, count=count, interval=interval, file_name=file_path)


def unicast_hop_test():
    count = 100
    size = 42
    interval = 1
    hops = 1
    test_name = "unicast_hop_test"
    ip_address = "fdde:ad00:beef:0:b351:6da2:9ed:4ebd"

    file_path = init(test_name=test_name, count=count, size=size, interval=interval, hops=hops)
    controller.ping(ipaddr=ip_address, size=size, count=count, interval=interval, file_name=file_path)

    """
    file_path = init(test_name=test_name)
    for interval in numpy.arange(0.5, 0.0009, -0.01):
        controller.ping(ipaddr=ip_address, size=12, count=count, interval=interval, file_name=file_path)

    file_path = init(test_name=test_name)
    for interval in numpy.arange(0.5, 0.0009, -0.01):
        controller.ping(ipaddr=ip_address, size=98, count=count, interval=interval, file_name=file_path)

    file_path = init(test_name=test_name)
    for interval in numpy.arange(0.5, 0.0009, -0.01):
        controller.ping(ipaddr=ip_address, size=198, count=count, interval=interval, file_name=file_path)
    """


controller = Controller.Controller()
unicast_hop_test()

"TODO: "
"""
def multicast_device_scale():
        
def unicast_interval_test():
    
def unicast_device_scale():
def unicast_hop_test():
    
"""

"ping fdde:ad00:beef:0:d6b6:4b50:de96:9861 392 5 "
"""
Plots als PDF nicht JPEG für Latex
        pandas zum Datenanalysis und ploten
        matplot lib
TODOs: 
    Referenzen: github, Papers, README
    Multicast Paketgrösse 8 - 1000
                Anzahl / Interval
                Geräteanzahl
    Unicast   
                Anzahl / Interval
                Geräteanzahl
                Hopanzahl

"""
