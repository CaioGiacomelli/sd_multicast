import process as pr
import message

p = [pr.Process(1), pr.Process(2), pr.Process(3)]

p[0].set_process_list(p)
p[1].set_process_list(p)
p[2].set_process_list(p)

p[0].send()
