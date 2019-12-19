import Controller

controller = Controller
"controller.console()"
Controller.append_row("test.csv", ipaddr="ff03::1", package_bytes=100, time=209)
"controller.ping('ff03::1', 100, 100, 1, 1)"
"""
pings = controller.ping_all()

TODO: Do this every ... interval
"""

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