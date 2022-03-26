import socket
import threading
import sys
from queue import Queue
import time
from ..messages import Messages
from ..user import User
import requests
from ...model.message import insert_message
import os

def run():
    users_dict = {}

    def recive_messages(conn, client, message_queue, users_list):
        
        while True:
            msg = conn.recv(1024).decode()
            if msg == 'exit' or msg == 'shutdown':
                break
            
            elif msg != '':
                if conn not in users_dict:
                        url = os.environ['APP_URL'] + '/generate_id'
                        id = requests.get(url).text
                        users_dict[conn] = User('None', id, conn, 'APP')

                
                insert_message(Messages(users_dict[conn], msg))
                print(Messages(users_dict[conn], msg))

        conn.send('exit'.encode())
        users_list.remove((conn, cliente))
        message_queue.put((client, msg))

        conn.close()
        

    def send_messages(message_queue, users_list):

        while True:
            if not(message_queue.empty()):
                message = message_queue.get()
                for user in users_list:
                    if message[0] != user[1] and message[1] != 'shutdown':
                        user[0].send(f'{user[1]} : {message[1]}'.encode())
                    
                    elif message[1] == 'shutdown':
                        user[0].send('exit'.encode())
            else:
                time.sleep(0.1)


    HOST = '127.0.0.1'     # Endereco IP do Servidor
    PORT = 4199            # Porta que o Servidor esta

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    orig = (HOST, PORT)

    tcp.bind(orig)
    tcp.listen(1)

    message_queue = Queue()
    users_list = []
    threading.Thread(target=send_messages, args=(message_queue, users_list)).start()

    while True:
        conn, cliente = tcp.accept()
        users_list.append((conn, cliente))
        threading.Thread(target=recive_messages, args=(conn, cliente, message_queue, users_list)).start()

    tcp.close()