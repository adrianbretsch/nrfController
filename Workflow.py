import Controller

controller = Controller.Controller("/dev/ttyACM0")

controller.ping(ipaddr="ff03::1",size=30,count=1)
"""Controller.append_row("test.csv", ipaddr="ff03::1", package_bytes=100, time=209)"""


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