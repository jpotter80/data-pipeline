from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class LLMAnalyzer:
    def __init__(self):
        # Initialize the OpenAI client with the API key from environment variables
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def analyze_structure(self, csv_structure: dict) -> str:
        # Prepare the prompt for CSV structure analysis
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

        # Make an API call to OpenAI for analysis
        response = self.client.chat.completions.create(
            model="gpt-4",  # Using GPT-4 for more advanced analysis
            messages=[
                {"role": "system", "content": "You are a data analyst expert."},
                {"role": "user", "content": prompt}
            ]
        )

        # Return the content of the first message in the response
        return response.choices[0].message.content

    def generate_sql_transformations(self, analysis: str) -> str:
        # Prepare the prompt for SQL transformation suggestions
        prompt = f"""
        Based on the following analysis, generate SQL statements for data cleaning and normalization:
        
        {analysis}
        
        Please provide SQL statements for:
        1. Handling null values
        2. Data type conversions
        3. Any necessary data transformations
        """

        # Make an API call to OpenAI for SQL transformations
        response = self.client.chat.completions.create(
            model="gpt-4",  # Using GPT-4 for more advanced SQL generation
            messages=[
                {"role": "system", "content": "You are a SQL expert."},
                {"role": "user", "content": prompt}
            ]
        )

        # Return the content of the first message in the response
        return response.choices[0].message.content