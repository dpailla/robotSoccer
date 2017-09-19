import socket
def do_connect(): #POSIBLEMENTE SEA PARA CONECTARNOS EN LA RED WIFI
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('CIDIS', 'labCid1$')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
do_connect()
IP_ESP8266=1921.25.2.3 #IP del servidor
PORT_ESP8266=8000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP_ESP8266,PORT_ESP8266))
s.send(dfSerial.encode(encoding="utd_8")) #dfSerial es lo que recibe del archivo master
s.close()