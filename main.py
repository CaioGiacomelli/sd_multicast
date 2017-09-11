import process as pr
import message
import copy
import threading

p = [pr.Process(1), pr.Process(2), pr.Process(3), pr.Process(4)]

p[0].set_process_list(p)
p[1].set_process_list(p)
p[2].set_process_list(p)
p[3].set_process_list(p)

p[0].send()

#
# m4 = message.Message(6)
#
# m1 = message.Message(5)
# m2 = message.Message(3)
# m3 = message.Message(1)
#
# queue = [(m3.ts, m3)]
# queue.append((m1.ts, m1))
# queue.append((m2.ts, m2))
#
# queue.sort()
#
# for x in queue:
#     print(x)
#     queue.remove(x)

# m5 = copy.copy(m4)
#
# print(m4)
# print(m5)
# print(m4.ts)
# print(m5.t

x = threading.current_thread()

print(x)