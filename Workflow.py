import Controller
from StringHelper import *


def multicast_package_benchmark():
    for size in range(2, 17, 8):
        controller.ping(size=size, interval=2, file_name="multicast-package-benchmark")


controller = Controller.Controller("/dev/ttyACM0")
multicast_package_benchmark()

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
