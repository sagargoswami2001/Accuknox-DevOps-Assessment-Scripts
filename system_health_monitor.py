import psutil
import logging
from datetime import datetime

# Configuration: thresholds
CPU_THRESHOLD = 80.0  # CPU usage percentage threshold
MEMORY_THRESHOLD = 80.0  # Memory usage percentage threshold
DISK_THRESHOLD = 80.0  # Disk space usage percentage threshold

# Set up logging
LOG_FILE = 'system_health.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU usage is high: {cpu_usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'Memory usage is high: {memory_usage}%')

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Disk usage is high: {disk_usage}%')

def check_running_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]
    if processes:
        logging.info(f'Running processes: {processes}')

def main():
    logging.info('System health check started')
    
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    
    logging.info('System health check completed')

if __name__ == '__main__':
    main()
