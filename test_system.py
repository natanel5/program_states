from main import get_cpu_usage, get_memory_usage, get_disk_usage
from alerts_check import check_alerts

def test_cpu_data(self):
    cpu_data = get_cpu_usage()
    print("CPU Data:", cpu_data)

def test_memory_data(self):
    memory_data = get_memory_usage()
    print("Memory Data:", memory_data)

def test_disk_data(self):
    disk_data = get_disk_usage()
    print("Disk Data:", disk_data)

def test_alerts(self):
    alerts = check_alerts()
    print("Alerts:", alerts)