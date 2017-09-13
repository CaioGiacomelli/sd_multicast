import message
from threading import Thread
import threading
import socket
import pickle
import copy


class MyThread (threading.Thread):

    def __init__(self, isack):

        threading.Thread.__init__(self)
        self.isack = isack
        # self.name = name
        # self.counter = counter

    def run(self):
        send_request(self.isack)


def send_request(isack):
    if not isack:
        option = input()
        while option != '2':
            if option == '1':
                for process in p:
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp.connect((host, process.port))
                    m1 = message.Message(5, isack)
                    m_dumped = pickle.dumps(m1)
                    x = tcp.send(m_dumped)
                    print(x)
                    tcp.close()
            option = input()
    else:
        for process in p:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.connect((host, process.port))
            m1 = message.Message(5, isack)
            m_dumped = pickle.dumps(m1)
            x = tcp.send(m_dumped)
            print(x)
            tcp.close()



#
# p[0].send()
#
# #
# # m4 = message.Message(6)
# #
# # m1 = message.Message(5)
# # m2 = message.Message(3)
# # m3 = message.Message(1)
# #
# # queue = [(m3.ts, m3)]
# # queue.append((m1.ts, m1))
# # queue.append((m2.ts, m2))
# #
# # queue.sort()
# #
# # for x in queue:
# #     print(x)
# #     queue.remove(x)
#
# # m5 = copy.copy(m4)
# #
# # print(m4)
# # print(m5)
# # print(m4.ts)
# # print(m5.t


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
        self.ts = 0
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



        while True:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            orig = (self.host, self.port)
            tcp.bind(orig)
            tcp.listen(1)

            con, cliente = tcp.accept()
            while True:
                msg = con.recv(1024)
                if msg:
                    msg_loaded = pickle.loads(msg)
                    new_m = copy.copy(msg_loaded)

                if not msg: break

            if not new_m.is_ack:
                for ack in self.acks:
                    if ack[0] - 1 == new_m.ts:
                        new_m.count += 1
                if new_m.count != len(self.process_list):
                    self.queue.append((new_m.ts, new_m))
                    self.queue.sort()

                thread3 = MyThread(1)
                thread3.start()
            else:

                found = False
                for check in self.queue:
                    if check[0] == new_m.ts - 1:
                        found = True
                        check[1].count += 1
                        if check[1].count == len(self.process_list):
                            self.queue.remove(check)

                if not found:
                    self.acks.append((new_m.ts, new_m))

            con.close()

host = '192.168.0.105'

p = [Process(1, host, 5000), Process(2, host, 5001), Process(3, host, 5002), Process(4, host, 5003)]

p[0].set_process_list(p)
p[1].set_process_list(p)
p[2].set_process_list(p)
p[3].set_process_list(p)

thread1 = MyThread(0)
thread1.start()


