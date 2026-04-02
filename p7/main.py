import os
import time
import logging
from datetime import datetime

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/app.log',
    filemode='w',
    level=logging.INFO,
)

def long_running_process():
    start_time = time.time()
    duration = 60
    interval = 5

    for _ in range(duration // interval):
        time.sleep(interval)
        elapsed = int(time.time() - start_time)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Програма працює {elapsed} секунд. Поточний час: {current_time}")

    logging.error("Task completed")

if __name__ == "__main__":
    long_running_process()
