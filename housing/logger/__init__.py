import logging
from datetime import datetime
import os

CURRENT_DATE = f"{datetime.now().strftime('%Y_%m_%d')}"
CURRENT_TIMESTAMP=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"

LOG_DIR=os.path.join("housing_logs",CURRENT_DATE)

LOG_FILE=f"log_{CURRENT_TIMESTAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )
