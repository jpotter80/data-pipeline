"""
Module for profiling CSV data.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any
import logging
import aiofiles
import io

logger = logging.getLogger(__name__)

class DataProfiler:
    def __init__(self, sample_size: int = 10):
        """
        Initialize the DataProfiler.

        Args:
            sample_size (int): Number of rows to sample for initial analysis.
        """
        self.sample_size = sample_size

    async def profile_csv(self, file_path: str) -> Dict[str, Any]:
        """
        Profile the CSV file and return a summary of its contents.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            Dict[str, Any]: Profile of the CSV file.
        """
        try:
            # Read the first few rows for initial analysis
            df_sample = await self._read_csv_sample(file_path)
            
            # Profile the entire file in chunks
            full_profile = await self._profile_full_file(file_path)
            
            return {
                "columns": df_sample.columns.tolist(),
                "sample_analysis": self._analyze_sample(df_sample),
                "full_profile": full_profile
            }
        except Exception as e:
            logger.error(f"Error profiling CSV file: {str(e)}")
            return {}

    async def _read_csv_sample(self, file_path: str) -> pd.DataFrame:
        """
        Read a sample of the CSV file asynchronously.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            pd.DataFrame: Sample of the CSV file.
        """
        async with aiofiles.open(file_path, mode='r') as f:
            content = await f.read(self.sample_size * 1024)  # Read a larger chunk to ensure we get enough rows
        return pd.read_csv(io.StringIO(content), nrows=self.sample_size)

    def _analyze_sample(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Analyze a sample of the dataframe to infer initial data types and structures.

        Args:
            df (pd.DataFrame): Sample dataframe to analyze.

        Returns:
            Dict[str, Any]: Analysis of the sample data.
        """
        analysis = {}
        for column in df.columns:
            column_type = df[column].dtype
            unique_values = df[column].nunique()
            sample_values = df[column].head().tolist()

            analysis[column] = {
                "inferred_type": str(column_type),
                "unique_values_in_sample": unique_values,
                "sample_values": sample_values
            }
        return analysis

    async def _profile_full_file(self, file_path: str, chunk_size: int = 10000) -> Dict[str, Any]:
        """
        Profile the entire CSV file in chunks to generate comprehensive statistics.

        Args:
            file_path (str): Path to the CSV file.
            chunk_size (int): Number of rows to process in each chunk.

        Returns:
            Dict[str, Any]: Full profile of the CSV file.
        """
        profile = {}
        async for chunk in self._read_csv_chunks(file_path, chunk_size):
            self._update_profile(profile, chunk)
        
        # Calculate final statistics
        for column in profile:
            profile[column]["null_percentage"] = (profile[column]["null_count"] / profile[column]["total_count"]) * 100
            if profile[column]["numeric"]:
                profile[column]["mean"] = profile[column]["sum"] / (profile[column]["total_count"] - profile[column]["null_count"])
        
        return profile

    async def _read_csv_chunks(self, file_path: str, chunk_size: int):
        """
        Generator to read CSV file in chunks asynchronously.

        Args:
            file_path (str): Path to the CSV file.
            chunk_size (int): Number of rows in each chunk.

        Yields:
            pd.DataFrame: Chunk of the CSV file.
        """
        async with aiofiles.open(file_path, mode='r') as f:
            chunk = await f.read(chunk_size * 1024)  # Read a chunk
            while chunk:
                yield pd.read_csv(io.StringIO(chunk))
                chunk = await f.read(chunk_size * 1024)  # Read the next chunk

    def _update_profile(self, profile: Dict[str, Any], chunk: pd.DataFrame):
        """
        Update the profile dictionary with statistics from a new chunk of data.

        Args:
            profile (Dict[str, Any]): Current profile to update.
            chunk (pd.DataFrame): New chunk of data.
        """
        for column in chunk.columns:
            if column not in profile:
                profile[column] = {
                    "total_count": 0,
                    "null_count": 0,
                    "unique_values": set(),
                    "numeric": True,
                    "min": None,
                    "max": None,
                    "sum": 0
                }
            
            profile[column]["total_count"] += len(chunk)
            profile[column]["null_count"] += chunk[column].isnull().sum()
            profile[column]["unique_values"].update(chunk[column].dropna().unique())
            
            if profile[column]["numeric"]:
                try:
                    numeric_data = pd.to_numeric(chunk[column].dropna())
                    profile[column]["min"] = min(profile[column]["min"] or numeric_data.min(), numeric_data.min())
                    profile[column]["max"] = max(profile[column]["max"] or numeric_data.max(), numeric_data.max())
                    profile[column]["sum"] += numeric_data.sum()
                except:
                    profile[column]["numeric"] = False
                    del profile[column]["min"]
                    del profile[column]["max"]
                    del profile[column]["sum"]

    def generate_report(self, profile: Dict[str, Any]) -> str:
        """
        Generate a human-readable report from the profile data.

        Args:
            profile (Dict[str, Any]): Profile data.

        Returns:
            str: Human-readable report.
        """
        report = "Data Profiling Report\n"
        report += "=====================\n\n"

        sample_analysis = profile.get("sample_analysis", {})
        full_profile = profile.get("full_profile", {})

        for column in full_profile:
            report += f"Column: {column}\n"
            report += f"  Inferred Type: {sample_analysis.get(column, {}).get('inferred_type', 'Unknown')}\n"
            report += f"  Total Count: {full_profile[column]['total_count']}\n"
            report += f"  Null Count: {full_profile[column]['null_count']}\n"
            report += f"  Null Percentage: {full_profile[column]['null_percentage']:.2f}%\n"
            report += f"  Unique Values: {len(full_profile[column]['unique_values'])}\n"
            
            if full_profile[column]["numeric"]:
                report += f"  Minimum: {full_profile[column]['min']}\n"
                report += f"  Maximum: {full_profile[column]['max']}\n"
                report += f"  Mean: {full_profile[column]['mean']:.2f}\n"
            
            report += f"  Sample Values: {', '.join(map(str, sample_analysis.get(column, {}).get('sample_values', [])))}\n"
            report += "\n"

        return report