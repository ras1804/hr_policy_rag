import logging
import os 
from logging.handlers import TimedRotatingFileHandler

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Base log file path. The handler will append the date to this filename at rollover.
DAILY_LOG_FILE = os.path.join(LOGS_DIR, "app.log")

# Create the daily rotating file handler
file_handler = TimedRotatingFileHandler(
    DAILY_LOG_FILE,
    when="midnight",     # Roll over every day at midnight
    interval=1,          # Repeat the rollover every 1 day
    backupCount=30,      # Optional: keeps logs for the last 30 days, deletes older ones
    encoding="utf-8"
)

# Crucial step: Set the filename suffix pattern for the rolled-over files (e.g., app.log.2026-09-19)
file_handler.suffix = "%Y-%m-%d"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
      file_handler,
      logging.StreamHandler(),
    ], 
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
