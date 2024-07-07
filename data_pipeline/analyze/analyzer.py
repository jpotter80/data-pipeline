"""
Module for AI-powered data analysis using the Anthropic API.
"""

import logging
from typing import Dict, Tuple, Optional
from anthropic import AsyncAnthropic
import aiofiles
import time
import json

logger = logging.getLogger(__name__)

class LLMAnalyzer:
    """Class for AI-powered data analysis."""

    def __init__(self, api_key: str):
        """
        Initialize the LLMAnalyzer.

        Args:
            api_key (str): Anthropic API key.
        """
        self.client = AsyncAnthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20240620"

    async def analyze_structure(self, csv_structure: Dict) -> Tuple[Optional[str], Optional[str]]:
        """
        Analyze the structure of CSV data using AI.

        Args:
            csv_structure (Dict): Structure of the CSV data.

        Returns:
            Tuple[Optional[str], Optional[str]]: Analysis result and log file path.
        """
        system_message = "You are an expert data analyst with extensive knowledge of data structures, data quality, and SQL. Your task is to analyze CSV data structures and provide insights and recommendations."

        simplified_structure = self._prepare_profile(csv_structure)
        
        user_message = f"""Analyze the following CSV structure and provide insights:
        
        Columns: {simplified_structure.get('columns', 'No column information available')}
        Data Types: {simplified_structure.get('sample_analysis', {})}
        Full Profile: {simplified_structure.get('full_profile', {})}
        
        Please provide:
        1. A summary of the data
        2. Potential data quality issues
        3. Suggestions for data cleaning and normalization"""

        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=system_message,
                messages=[{"role": "user", "content": user_message}]
            )

            analysis = response.content[0].text
            log_file = await self.log_interaction(user_message, analysis, "structure_analysis")
            return analysis, log_file

        except Exception as e:
            logger.error(f"An error occurred during structure analysis: {e}")
            return None, None

    async def generate_sql_transformations(self, analysis: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Generate SQL transformations based on the analysis.

        Args:
            analysis (str): Analysis of the data structure.

        Returns:
            Tuple[Optional[str], Optional[str]]: SQL transformations and log file path.
        """
        system_message = "You are an expert SQL developer. Your task is to generate SQL transformations based on the provided data analysis."

        user_message = f"""Based on the following data analysis, generate SQL transformations to address the identified issues and implement the suggested improvements:

        {analysis}

        Please provide:
        1. SQL statements for data cleaning
        2. SQL statements for data normalization
        3. Any additional SQL transformations that would improve data quality"""

        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=system_message,
                messages=[{"role": "user", "content": user_message}]
            )

            sql_transformations = response.content[0].text
            log_file = await self.log_interaction(user_message, sql_transformations, "sql_transformations")
            return sql_transformations, log_file

        except Exception as e:
            logger.error(f"An error occurred during SQL transformation generation: {e}")
            return None, None

    async def log_interaction(self, user_message: str, ai_response: str, interaction_type: str) -> str:
        """
        Log the interaction between the user and AI.

        Args:
            user_message (str): User's message.
            ai_response (str): AI's response.
            interaction_type (str): Type of interaction.

        Returns:
            str: Path to the log file.
        """
        timestamp = time.time()
        log_filename = f"{interaction_type}_{timestamp}.log"
        
        try:
            async with aiofiles.open(log_filename, mode='w') as log_file:
                await log_file.write(f"User Message:\n{user_message}\n\nAI Response:\n{ai_response}")
            logger.info(f"Interaction logged to {log_filename}")
            return log_filename
        except Exception as e:
            logger.error(f"Error logging interaction: {e}")
            return None

    def _prepare_profile(self, profile: Dict) -> Dict:
        """
        Prepare the profile data for AI analysis.

        Args:
            profile (Dict): Raw profile data.

        Returns:
            Dict: Simplified profile data.
        """
        def simplify(obj):
            if isinstance(obj, (int, float, str, bool, type(None))):
                return obj
            elif isinstance(obj, (list, tuple)):
                return [simplify(item) for item in obj]
            elif isinstance(obj, dict):
                return {str(key): simplify(value) for key, value in obj.items()}
            elif isinstance(obj, set):
                return list(obj)
            return str(obj)

        return simplify(profile)

    @staticmethod
    def _convert_to_serializable(obj):
        """
        Convert an object to a JSON serializable format.

        Args:
            obj: The object to convert.

        Returns:
            A JSON serializable representation of the object.
        """
        if isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        elif isinstance(obj, (list, tuple)):
            return [LLMAnalyzer._convert_to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {str(key): LLMAnalyzer._convert_to_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, set):
            return list(obj)
        return str(obj)