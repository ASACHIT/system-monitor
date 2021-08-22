import os
import platform
import time

import GPUtil
import psutil
from termcolor import colored


def unit(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def clr(text):
    colorgrn = colored(f"{text}", "green")
    return colorgrn


def monitor():
    time.sleep(1.5)
    gpus = GPUtil.getGPUs()
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    mem = psutil.virtual_memory()
    gpus = GPUtil.getGPUs()
    internet = psutil.net_io_counters()
    sys = uname.system
    core = psutil.cpu_count(logical=True)
    cpu_freq_mx = cpufreq.max
    mem_total = (int(mem.total)) / (1024 * 1024 * 1024)

    gpu_list = []
    for gpu in gpus:
        gpu_name = gpu.name
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_list.append((gpu_name, gpu_total_memory))

    g_pu = (gpu_list[0])[0]
    g_pu_mem = (gpu_list[0])[1]
    os.system("clear")
    print(
        f"""
    {"="*20} SYSTEM Info {"="*20}
            System       - {colored(sys,"green", attrs=["bold"])}
            Total Cores  - {clr(f"{core} Cores")} 
            Cpu Usage    - {clr(f"{psutil.cpu_percent()}%")}
            Max Cpu Freq - {clr(f"{cpu_freq_mx}MHZ")}
            Total Ram    - {clr(f"{round(mem_total)}GB")}
            Ram in Use   - {clr(f"{unit(mem.used)}")} | {clr(f"{mem.percent}%")}
            Gpu          - {clr(g_pu)}
            Gpu Memory   - {clr(g_pu_mem)}
    {"="*20} Internet {"="*24}        
            Data Sent    - {clr(unit(internet.bytes_sent))}
            Data Receive - {clr(unit(internet.bytes_recv))}
                                    
    """
    )


while True:
    monitor()
