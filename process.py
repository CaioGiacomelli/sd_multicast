import message

class Process:

    def __init__(self, pid):
        self.pid = pid
        self.ts = 0
        self.queue = queue()
        self.ack_vector = []

    def receive(self, message):
        pass

    def send(self, process_list):
        message = message.Message(process_list, self.ts)
        self.ts = self.ts + 1
        message.send()
