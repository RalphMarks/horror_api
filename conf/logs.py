"""
Custom loggin classes
"""
import logging


class ConsoleLevelFilter(logging.Filter):
    """
    Custom console level filter
    """

    def filter(self, record):
        return record.levelno < logging.ERROR
