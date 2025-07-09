from socket import socket, AF_INET, SOCK_STREAM
import time
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 12345))
sock.listen(5)
sock.setblocking(False)

players = {} 
conn_ids = {}
id_counter = 0


def handl_data():
    global id_counter
    while True:
        time.sleep(0.01)
        player_data = {}
        to_remove = {}

        for conn in list(players):
            try:
                data = conn.recv(64).decode().strip()
                if ',' in data:
                    parts = data.split(',')
                    if len(parts) == 4:
                        pid,x,y,r = map(int, parts)
                        players[conn] = {'id': pid, 'x':x, 'y':y,'r':r}
                        player_data[conn] = players[conn]
            except:
                continue

Thread(target = handl_data, deamon = True).start()

print('SERVER runing...')

while True:
    try:
        conn, adr =sock.accept()
        conn.setblocking(False)
        id_counter += 1
        players[conn] = {'id': id_counter, 'x':0, 'y':0, 'r':20}
        conn_ids[conn]
        conn.send(f'{id_counter}, 0,0,20'.encode())
    except:
        pass
    










conn, adr = sock.accept()