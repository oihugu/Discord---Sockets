import socket
import threading
import time
import requests
import os

users_dict = {}

def recive_messages(conn):
    while True:
        msg = conn.recv(1024).decode()

        if msg == 'exit':
            break

        print(msg)

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 4199            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
conn = tcp.connect(dest)

recive_thread = threading.Thread(target=recive_messages, args=[tcp])
recive_thread.start()

msg = input()

while msg != 'exit' and msg != 'shutdown':
    tcp.send(msg.encode())
    msg = input()

tcp.send(msg.encode())
time.sleep(0.5)
tcp.close()