import Controller

serial = Controller.init_serial("/dev/ttyACM0")
"""
TODO: Do this every ... interval
"""
Controller.ping_all(serial)

