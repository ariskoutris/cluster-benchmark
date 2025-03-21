
from time import sleep
import psutil
from datetime import datetime
import csv

fields = ['timestamp', 'cpu']

def measure_cpu():
    memcached_pid = None
    for proc in psutil.process_iter():
        if proc.name() == "memcached":
            memcached_pid = proc.pid
            break
    
    if memcached_pid is None:
        raise Exception("Memcached PID not found...")
    memcached_proc = psutil.Process(memcached_pid)
    filename = "cpu_util.csv"
    mc_cpu_usage = memcached_proc.cpu_percent()
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        while True:
            mc_cpu_usage = memcached_proc.cpu_percent()
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            row = {'timestamp': int(timestamp), 'cpu': mc_cpu_usage}

            writer.writerow(row)
            
            sleep(0.1)
            break


if __name__ == "__main__":
    measure_cpu()
