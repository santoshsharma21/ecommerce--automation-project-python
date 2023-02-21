# import libraries
import inspect
import logging


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="A:/AutomationProjects_python/ecommerce_app/logs/online_shop.log",
                            level=logging.INFO, force=True, format="%(asctime)s: %(levelname)s: %(name)s: %("
                                                                   "funcName)s(): %(message)s:",
                            datefmt="%d-%b-%Y %H:%M:%S")
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger
