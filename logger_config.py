import logging
from colorama import Fore , Style

def setup_logger():
    logger=logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    file_handler=logging.FileHandler("logs/bots.log")
    console_handler=logging.StreamHandler()

    formatter=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger