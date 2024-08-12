import re
from collections import Counter
import logging

# Configuration
LOG_FILE_PATH = '/var/log/nginx/access.log' # Path to your web server log file
REPORT_FILE = 'log_report.txt'  # Path to save the report

# Set up logging
logging.basicConfig(filename=REPORT_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_logs(log_file_path):
    # Initialize counters
    error_404_count = 0
    page_requests = Counter()
    ip_requests = Counter()

    # Regular expression pattern for Apache/Nginx common log format
    log_pattern = re.compile(
        r'(?P<ip>\S+) \S+ \S+ \[.*?\] "(?:GET|POST|PUT|DELETE) (?P<url>\S+) .*?" \d+ (?P<status>\d+)'
    )

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = log_pattern.match(line)
                if match:
                    ip = match.group('ip')
                    url = match.group('url')
                    status = match.group('status')

                    # Count 404 errors
                    if status == '404':
                        error_404_count += 1

                    # Count page requests
                    page_requests[url] += 1

                    # Count IP addresses
                    ip_requests[ip] += 1

        # Generate report
        logging.info('Log file analysis report')
        logging.info(f'Total 404 errors: {error_404_count}')
        
        logging.info('Most requested pages:')
        for page, count in page_requests.most_common(10):
            logging.info(f'{page}: {count} requests')

        logging.info('IP addresses with the most requests:')
        for ip, count in ip_requests.most_common(10):
            logging.info(f'{ip}: {count} requests')

    except FileNotFoundError:
        logging.error(f'Log file not found: {log_file_path}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

def main():
    logging.info('Starting log file analysis.')
    analyze_logs(LOG_FILE_PATH)
    logging.info('Log file analysis completed.')

if __name__ == '__main__':
    main()
