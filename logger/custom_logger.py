import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)
        self.log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, self.log_file)
        
        logging.basicConfig(
            filename=self.log_file_path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    
    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__ == "__main__":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Logging setup complete.")