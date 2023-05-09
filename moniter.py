#!/usr/bin/env python
import time
import psutil

pid=0


def get_pid(name):
    global pid
    pids = psutil.process_iter()
    for sb in pids:
        if(sb.name() == name):
            pid=sb.pid
    print("[" + name + "]'s pid is: ")

get_pid("fastlio_mapping")


# get process
p = psutil.Process(pid)

# monitor process and write data to file
interval = 3 # polling seconds
with open("/home/crz/al-huace/Spin-LIO/src/Spin-LIO/Log/process_monitor_" + p.name() + '_' + str(pid) + ".csv", "a+") as f:
	f.write("time,cpu%,mem%\n") # titles
	while True:
		current_time = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
		cpu_percent = p.cpu_percent() # better set interval second to calculate like:  p.cpu_percent(interval=0.5)
		mem_percent = p.memory_percent()
		line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent)
		print (line)
		f.write(line + "\n")
		time.sleep(interval)
