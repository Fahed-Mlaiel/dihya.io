import logging
import json
from pythonjsonlogger import jsonlogger

class StructuredLogger:
    def __init__(self, name=__name__, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        log_handler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter(
            fmt='%(asctime)s %(name)s %(levelname)s %(message)s'
        )
        log_handler.setFormatter(formatter)
        self.logger.addHandler(log_handler)

    def get_logger(self):
        return self.logger

    def info(self, message, **kwargs):
        self.logger.info(message, extra=kwargs)

    def error(self, message, **kwargs):
        self.logger.error(message, extra=kwargs)

    def warning(self, message, **kwargs):
        self.logger.warning(message, extra=kwargs)

    def debug(self, message, **kwargs):
        self.logger.debug(message, extra=kwargs)

    def critical(self, message, **kwargs):
        self.logger.critical(message, extra=kwargs)

# Usage example
if __name__ == "__main__":
    logger = StructuredLogger(name="my_application").get_logger()
    logger.info("Application started")
    logger.error("An error occurred", extra={"user": "admin", "section": "billing"})