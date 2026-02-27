import logging

def setup_logger(log_file: str = "nfl_stats.log"):
    logger = logging.getLogger("nfl_stats")
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(ch)

        # File handler
        fh = logging.FileHandler(log_file)
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(fh)

    return logger

logger = setup_logger()