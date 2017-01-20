
from machine import Timer
from ntptime import settime

rtc = settime()

def take_reading(rtc):
    import maxsonar
    from report import report_height
    from time import mktime
    from time import sleep_ms
    maxsonar.start_ranging()
    sleep_ms(100)
    height = maxsonar.distance()
    report_height(mktime(rtc.now()), height)
    maxsonar.stop_ranging()

take_reading(rtc)
alarm = Timer.Alarm(handler=take_reading, s=60, arg=rtc, periodic=True)
