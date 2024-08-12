import requests
import logging
from datetime import datetime

# Configuration
APPLICATION_URL = 'https://sagargoswami2001.github.io/2048-Game-Using-Docker'  # URL of the application to check
STATUS_OK_CODES = {200, 201, 202, 204}  # HTTP status codes considered as 'up'
STATUS_DOWN_CODES = {400, 404, 500, 503}  # HTTP status codes considered as 'down'
LOG_FILE = 'application_health.log'  # Path to save the health check log

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_application_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        
        if status_code in STATUS_OK_CODES:
            status = 'up'
            logging.info(f'Application is up. Status code: {status_code}')
        elif status_code in STATUS_DOWN_CODES:
            status = 'down'
            logging.warning(f'Application is down. Status code: {status_code}')
        else:
            status = 'unknown'
            logging.warning(f'Application status is unknown. Status code: {status_code}')
        
        return status
    
    except requests.RequestException as e:
        logging.error(f'An error occurred while checking the application: {e}')
        return 'error'

def main():
    logging.info('Starting application health check.')
    status = check_application_status(APPLICATION_URL)
    logging.info(f'Application health check completed. Status: {status}')

if __name__ == '__main__':
    main()
