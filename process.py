

class Process:

    def __init__(self, pid):
        self.pid = pid
        self.ts = 0
        self.queue = queue()
        self.ack_vector = []

    def receive(self, message):
        pass
