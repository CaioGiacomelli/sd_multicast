import message
import queue as Q


class Process:

    def __init__(self, pid):
        self.pid = pid
        self.ts = 0
        self.queue = Q.PriorityQueue()
        self.ack_vector = []
        self.process_list = []

    def set_process_list(self, process_list):
        self.process_list = process_list

    def receive(self, m):
        self.queue.put(m.ts, m)
        print("era pra ser 3 mensagens dessa")
        m.send_ack(self.process_list)
        pass

    def send(self):
        m = message.Message(self.ts)
        self.ts = self.ts + 1
        m.send(self.process_list)

    def receive_ack(self, m):
        pass
