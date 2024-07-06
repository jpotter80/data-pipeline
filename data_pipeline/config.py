"""
Configuration management for the data pipeline project.
"""

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
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
        # Add more validation as needed