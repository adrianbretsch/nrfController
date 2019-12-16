import Controller

serial = Controller.init_serial("/dev/ttyACM0")
Controller.ping_all(serial)

