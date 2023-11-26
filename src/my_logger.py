import logging.config
import os


def get_logger() -> logging.Logger:
    path_config = os.path.join("logging_config.ini")
    if os.path.isfile(path_config):
        logging.config.fileConfig(fname=path_config)
        my_logger = logging.getLogger("my_logger")
        return my_logger
    else:
        my_logger = logging.getLogger("logger")
        my_logger.setLevel("DEBUG")
        file_handler = logging.FileHandler(filename="logging.log", mode="w", encoding="UTF-8")
        file_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(filename)s-%(funcName)s: %(message)s", datefmt="%d.%m.%Y-%H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        my_logger.addHandler(file_handler)
        return my_logger


logger = get_logger()
