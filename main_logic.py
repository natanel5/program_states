import time
from main import get_cpu_usage, get_memory_usage, get_disk_usage, get_processes_usage
from alerts_check import check_alerts
from display import show_data


def main():
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        processes_usage = get_processes_usage()
        alerts = check_alerts(cpu_usage, memory_usage, disk_usage, processes_usage)
        show_data(cpu_usage, memory_usage, disk_usage, processes_usage, alerts)
        time.sleep(1)


if __name__ == "__main__":
    main()
