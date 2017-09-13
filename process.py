import message

import copy
import threading
import socket
import pickle
import main


class MyThread (threading.Thread):

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
        thread2 = MyThread(self)
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

                thread3 = main.MyThread(1)
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

