import socket

def report_height(time, height):
    address = ('192.168.1.8', 80)
    content = "time=" + str(time) + "&height=" + str(height)
    request = str.encode("POST /report HTTP/1.1\r\n" +
        "Host: " + address[0] + "\r\n" +
        "User-Agent: drainwatcher/1.0\r\n" +
        "Connection: close\r\n" +
        "Content-Type: application/x-www-form-urlencoded;\r\n" +
        "Content-Length: " + str(len(content)) + "\r\n\r\n" +
        content)
    s = socket.socket()
    s.connect(address)
    s.send(request)
    response = s.recv(1024)
    return response
