import logging.config
import os


def get_logger():
    log_config_path = os.path.join("..", "logging_config1.ini")
    if os.path.isfile(log_config_path):
        logging.config.fileConfig(fname=log_config_path)
        my_logger = logging.getLogger("my_logger")
        return my_logger
    else:
        my_logger = logging.getLogger("logger")
        my_logger.setLevel("DEBUG")
        file_handler = logging.FileHandler(filename="logging.log")
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(filename)s-%(funcName)s: %(message)s",
            datefmt="%d.%m.%Y-%H:%M:%S")
        file_handler.setFormatter(file_formatter)
        my_logger.addHandler(file_handler)
        return my_logger


logger = get_logger()
