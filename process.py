import message
import queue as Q
import copy


class Process:

    def __init__(self, pid):
        self.pid = pid
        self.ts = 0
        self.queue = []
        self.acks = []
        self.process_list = []

    def set_process_list(self, process_list):
        self.process_list = process_list

    def receive(self, m):
        new_m = copy.copy(m)

        for ack in self.acks:
            if ack[0] - 1 == new_m.ts:
                new_m.count += 1

        if new_m.count != len(self.process_list):

            self.queue.append((new_m.ts, new_m))
            self.queue.sort()

        m_ack = message.Message(new_m.ts + 1)
        m_ack.send_ack(self.process_list)

    def send(self):
        m = message.Message(self.ts)
        self.ts = self.ts + 1
        m.send(self.process_list)

    def receive_ack(self, m):
        found = False
        for check in self.queue:
            if check[0] == m.ts - 1:
                found = True
                check[1].count += 1
                if check[1].count == len(self.process_list):
                    self.queue.remove(check)
                    print(self.pid, len(self.acks))

        if not found:
            self.acks.append((m.ts, m))
