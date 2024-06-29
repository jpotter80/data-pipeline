import openai
import os
from dotenv import load_dotenv

load_dotenv()

class LLMAnalyzer:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def analyze_structure(self, csv_structure: dict) -> str:
        prompt = f"""
        Analyze the following CSV structure and provide insights:
        
        Columns: {csv_structure['columns']}
        Data Types: {csv_structure['dtypes']}
        Sample Data: {csv_structure['sample_data']}
        Null Counts: {csv_structure['null_counts']}
        Row Count: {csv_structure['row_count']}
        
        Please provide:
        1. A summary of the data
        2. Potential data quality issues
        3. Suggestions for data cleaning and normalization
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a data analyst expert."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    def generate_sql_transformations(self, analysis: str) -> str:
        prompt = f"""
        Based on the following analysis, generate SQL statements for data cleaning and normalization:
        
        {analysis}
        
        Please provide SQL statements for:
        1. Handling null values
        2. Data type conversions
        3. Any necessary data transformations
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a SQL expert."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content