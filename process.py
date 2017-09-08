import message
import queue


class Process:

    def __init__(self, pid, process_list):
        self.pid = pid
        self.ts = 0
        self.queue = queue.PriorityQueue()
        self.ack_vector = []
        self.process_list = process_list

    def receive(self, m):
        pass

    def send(self):
        m = message.Message(self.process_list, self.ts)
        self.ts = self.ts + 1
        m.send()