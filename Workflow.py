import datetime

import Controller
from StringHelper import *
import numpy


def init(test_name):
    now = datetime.datetime.now()
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


def multicast_package_benchmark():
    test_name = "multicast-package-benchmark"
    file_path = init(test_name)
    for size in range(2, 17, 8):
        controller.ping(size=size, interval=2, file_name=file_path)


def multicast_interval_benchmark():
    file_name = test_name = "multicast-interval-benchmark"
    init(test_name)
    "smallest 0.001"
    for interval in numpy.arange(0.01, 0.0009, -0.001):
        file_name = controller.ping(size=392, interval=interval, file_name=file_name)


controller = Controller.Controller("/dev/ttyACM0")
multicast_package_benchmark()

"ping fdde:ad00:beef:0:d6b6:4b50:de96:9861 392 5 "
"""
Plots als PDF nicht JPEG für Latex
        pandas zum Datenanalysis und ploten
        matplot lib
TODOS: 
Referenzen: github, Papers
Multicast Paketgrösse 8 - 1000
            Anzahl / Interval
            Geräteanzahl
Unicast   Paketgösse 8 -1000
            Anzahl / Interval
            Geräteanzahl
            Hopanzahl

"""
