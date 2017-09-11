

class Message:

    def __init__(self, ts):
        self.ts = ts
        self.count = 0
        pass

    def send(self, process_list):
        for process in process_list:
            process.receive(self)

    def send_ack(self, process_list):
        for process in process_list:
            process.receive_ack(self)