

class Message:

    def __init__(self, ts):
        self.ts = ts
        pass

    def send(self, process_list):
        for p in process_list:
            p.receive(self)