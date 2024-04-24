import logging
import os
from datetime import datetime
# This file will log out the date and time as the file name

# Get the current date and time and change to string
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Get the current directory
log_path=os.path.join(os.getcwd(),"logs")

# if not created logs directory
os.makedirs(log_path,exist_ok=True)

# Finalize the complete file path 
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

# Final output of the file, using some configuration for the level (6 level in logging python)
logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)