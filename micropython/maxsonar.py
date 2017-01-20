from machine import Pin
from machine import UART
import time
import _thread

rpin = Pin('P6',  Pin.OPEN_DRAIN)
rpin(False)
uart = UART(0,  9600)

d = 0
lock = _thread.allocate_lock()
ranging = False

def start_ranging():
    _thread.start_new_thread(distance_read_thread,())

def stop_ranging():
    global ranging
    ranging = False

def distance_read_thread():
    """To be run as a thread, continuously reads
    uart."""
    global d, ranging
    ranging = True
    uart.init(9600,  8,  None,  1)
    rpin(True)
    while ranging:
        if uart.any() >= 5:
            db = uart.read(5)
            di = int(db[1:4])
            with lock:
                d = di
        else:
            time.sleep_ms(100)
    rpin(False)
    uart.deinit()

def distance():
    """Return distance as int."""
    with lock:
        return d
