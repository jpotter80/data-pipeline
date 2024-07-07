"""
Configuration management for the data pipeline project.
"""

import os
import re
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

class Config:
    """Manages configuration settings for the data pipeline project."""

    def __init__(self):
        self.data_dir = Path('dataset')
        self.output_dir = Path('visualizations')
        self.db_config = {
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASS'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432')
        }
        self.anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

    def validate(self):
        """Validate the configuration."""
        if not self.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set in the environment.")
        if not self.db_config['password']:
            raise ValueError("DB_PASS is not set in the environment.")

        # Validate database configuration
        self._validate_db_config()

        # Validate directory paths
        self._validate_directory(self.data_dir, "Data directory")
        self._validate_directory(self.output_dir, "Output directory")

    def _validate_db_config(self):
        """Validate database configuration parameters."""
        # Check if the user contains only allowed characters
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', self.db_config['user']):
            raise ValueError(f"Invalid database user: {self.db_config['user']}")

        # Validate host (simple check for now, can be expanded)
        if not self.db_config['host']:
            raise ValueError("Database host is not specified")

        # Validate port
        try:
            port = int(self.db_config['port'])
            if port <= 0 or port > 65535:
                raise ValueError(f"Invalid port number: {port}")
        except ValueError as exc:
            raise ValueError(f"Invalid port: {self.db_config['port']}") from exc

    def _validate_directory(self, path: Path, dir_type: str):
        """Validate if a directory exists and is accessible."""
        if not path.exists():
            raise ValueError(f"{dir_type} does not exist: {path}")
        if not path.is_dir():
            raise ValueError(f"{dir_type} is not a directory: {path}")
        if not os.access(path, os.R_OK | os.W_OK):
            raise ValueError(f"{dir_type} is not readable and writable: {path}")