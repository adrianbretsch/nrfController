import datetime

import Controller
from StringHelper import *
import numpy


def init(test_name, interval=0):
    now = datetime.datetime.now()
    if not interval == 0:
        file_name = "{}_i-{}.csv".format(test_name, interval)
    else:
        file_name = "{}_{}.csv".format(test_name, now.strftime("%x_%X").replace(":", "-").replace("/", "-"))
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
    for size in range(2, 992, 10):
        controller.ping(size=size, file_name=file_path)


def multicast_interval_test():
    test_name = "multicast-interval-test"
    "smallest 0.001"
    for interval in numpy.arange(0.7, 0.0009, -0.01):
        file_path = init(test_name=test_name, interval=interval)
        controller.ping(size=12, count=20, interval=interval, file_name=file_path)


def multicast_stability_test():
    test_name = "multicast-stability-test"
    for interval in numpy.arange(1, 0.0009, -0.005):
        file_path = init(test_name=test_name, interval=interval)
        controller.ping(size=12, count=20, interval=interval, file_name=file_path)


controller = Controller.Controller()
multicast_package_test()

"TODO: "

"""
def multicast_device_scale():
    
def unicast_package_test():
    
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
    Unicast   Paketgösse 8 -1000
                Anzahl / Interval
                Geräteanzahl
                Hopanzahl

"""
