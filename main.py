import message
from threading import Thread
import threading
import socket
import pickle
import copy
import time
import os

class MyThread (threading.Thread):

    def __init__(self, isack, pro, ts_ack):

        threading.Thread.__init__(self)
        self.isack = isack
        self.pro = pro
        self.ts_ack = ts_ack
        # self.name = name
        # self.counter = counter

    def run(self):
        send_request(self.isack, self.pro, self.ts_ack)


def send_request(isack, pro, ts_ack):

    if not isack:
        message_ts = str(pro.ts) + str(pro.pid)
        message_ts = int(message_ts)
        print("TS da mensagem enviada: ", message_ts)
        for process in p:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.connect((host, process.port))
            m1 = message.Message(message_ts, isack)
            m_dumped = pickle.dumps(m1)
            x = tcp.send(m_dumped)
            tcp.close()
        pro.ts += 1

    else:
        for process in p:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.connect((host, process.port))
            m1 = message.Message(ts_ack, isack)
            m_dumped = pickle.dumps(m1)
            x = tcp.send(m_dumped)
            tcp.close()


class MyThread2 (threading.Thread):

    def __init__(self, pr):

        threading.Thread.__init__(self)
        self.process = pr
        # self.name = name
        # self.counter = counter

    def run(self):
        Process.receive(self.process)


class Process:

    def __init__(self, pid, host, port):
        self.pid = pid
        self.ts = 1
        self.queue = []
        self.acks = []
        self.process_list = []
        self.host = host
        self.port = port
        thread2 = MyThread2(self)
        thread2.start()

    def set_process_list(self, process_list):
        self.process_list = process_list

    def receive(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self.host, self.port)
        tcp.bind(orig)
        tcp.listen(1)

        while True:

            con, cliente = tcp.accept()

            while True:
                msg = con.recv(1024)
                if msg:
                    msg_loaded = pickle.loads(msg)
                    new_m = copy.copy(msg_loaded)

                if not msg: break

            con.close()
            if not new_m.is_ack:
                for ack in self.acks:
                    if ack[0] - 1 == new_m.ts:
                        new_m.count += 1
                if new_m.count != len(self.process_list):

                    self.queue.append((new_m.ts, new_m))
                    self.queue.sort(key=lambda tup: tup[0])

                message_ts = str(self.ts) + str(self.pid)
                message_ts = int(message_ts)
                while (new_m.ts > message_ts):
                    self.ts += 1
                    message_ts = str(self.ts) + str(self.pid)
                    message_ts = int(message_ts)

                thread3 = MyThread(1, self, (new_m.ts + 1))
                thread3.start()
            else:
                found = False

                for check in self.queue:
                    if check[0] == new_m.ts - 1:
                        found = True
                        check[1].count += 1
                        if check[1].count == len(self.process_list):
                            print('Removendo da fila a mensagem com ts: ', new_m.ts-1, 'enviada para a porta: ', self.port)
                            self.queue.remove(check)


                if not found:
                    self.acks.append((new_m.ts, new_m))


host = '192.168.0.105'
p = []
process_number = 1

print("1 - Cria Processo")
print("2 - Enviar Mensagem")
print("3 - Sair")
option = input()

while True:

    if option == '1':
        port_number = 5000 + process_number
        p.append(Process(process_number, host, port_number))
        process_number += 1
        for proc in p:
            proc.set_process_list(p)

    elif option == '2':
        print("Qual processo enviará a mensagem?")
        sender = int(input())
        thread1 = MyThread(0, p[sender-1], 0)
        thread1.start()

    elif option == '3':
        os._exit(0)

    print("1 - Cria Processo")
    print("2 - Enviar Mensagem")
    print("3 - Sair")
    option = input()


