
try:
    import usocket as socket
except:
    import socket
try:
    import ustruct as struct
except:
    import struct

# (date(1970, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 2208988800

host = "se.pool.ntp.org"

def time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    addr = socket.getaddrinfo(host, 123)[0][-1]
    #addr = ('216.58.214.164', 123)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA

# There's currently no timezone support in MicroPython, so
# utime.localtime() will return UTC time (as if it was .gmtime())
def settime():
    t = time()
    import machine
    from time import localtime
    tm = localtime(t)
    rtc = machine.RTC()
    rtc.init(tm)
    return rtc
