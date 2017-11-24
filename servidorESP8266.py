import socket
def servidor(IP_esp8266):
    sock = socket.socket()
    addrinfos = socket.getaddrinfo("200.126.19.104", 1234)
    sock.connect(addrinfos[0][4])
    sock.send("Hello World!")
    sock.close()

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('LOGIN', 'PASSW')
        while not sta_if.isconnected():
            pass
    tupla_datos=sta_if.ifconfig()
    global IP_esp8266
    IP_esp8266=tupla_datos[0]
    print('network config:', sta_if.ifconfig())
    return IP_esp8266
do_connect()
print(servidor(IP_esp8266))