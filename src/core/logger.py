"""
Logger configuration and setup for the system.
"""

import logging
import logging.config
import json
from pathlib import Path
from typing import Optional
import yaml


class StructuredLogger:
    """Wrapper for structured logging with JSON support."""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
    
    def debug(self, message: str, **kwargs):
        """Log debug message."""
        self._log_structured("DEBUG", message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message."""
        self._log_structured("INFO", message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message."""
        self._log_structured("WARNING", message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message."""
        self._log_structured("ERROR", message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message."""
        self._log_structured("CRITICAL", message, **kwargs)
    
    def _log_structured(self, level: str, message: str, **kwargs):
        """Log with structured data."""
        log_data = {
            "level": level,
            "message": message,
            **kwargs
        }
        
        log_method = getattr(self.logger, level.lower())
        log_method(json.dumps(log_data))


def setup_logging(config_path: str = "configs/logging.yaml") -> None:
    """Setup logging from configuration file."""
    
    if not Path(config_path).exists():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Ensure log directories exist
    for handler_config in config.get('handlers', {}).values():
        if 'filename' in handler_config:
            log_file = Path(handler_config['filename'])
            log_file.parent.mkdir(parents=True, exist_ok=True)
    
    logging.config.dictConfig(config)


def get_logger(name: str) -> StructuredLogger:
    """Get a structured logger instance."""
    return StructuredLogger(name)
