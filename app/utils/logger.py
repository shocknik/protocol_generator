from loguru import logger
import sys
from pathlib import Path
from config import LOG_PATH

def setup_logger():
    logger.remove()
    
    # Консольный вывод
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )
    
    # Файловый вывод
    logger.add(
        LOG_PATH,
        rotation="1 week",
        retention="1 month",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {module}:{function}:{line} - {message}",
        level="DEBUG",
        enqueue=True
    )
    
    return logger

# Глобальный логгер
logger = setup_logger()