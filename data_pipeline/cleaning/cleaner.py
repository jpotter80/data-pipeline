"""
Module for cleaning and transforming data.
"""

import logging
from typing import Dict, Any
import pandas as pd

logger = logging.getLogger(__name__)

class DataCleaner:
    """Class for cleaning and transforming data."""

    async def clean_data(self, df: pd.DataFrame, profile: Dict[str, Any]) -> pd.DataFrame:
        """
        Clean and transform the dataframe based on profiling results.

        Args:
            df (pd.DataFrame): Input DataFrame to clean.
            profile (Dict[str, Any]): Profile data for the DataFrame.

        Returns:
            pd.DataFrame: Cleaned DataFrame.
        """
        cleaned_df = df.copy()
        
        for column, info in profile['full_profile'].items():
            if column not in cleaned_df.columns:
                continue

            cleaned_df[column] = await self._clean_column(cleaned_df[column], info)

        return cleaned_df

    async def _clean_column(self, series: pd.Series, info: Dict[str, Any]) -> pd.Series:
        """
        Clean a single column based on its profile information.

        Args:
            series (pd.Series): Column data to clean.
            info (Dict[str, Any]): Profile information for the column.

        Returns:
            pd.Series: Cleaned column data.
        """
        if info['null_percentage'] > 50:
            logger.warning(
                f"Column {series.name} has {info['null_percentage']:.2f}% null values. "
                "Consider dropping this column."
            )
        
        if info['numeric']:
            return pd.to_numeric(series, errors='coerce')
        elif info.get('date_detected', False):
            return pd.to_datetime(series, errors='coerce')
        else:
            return series.astype(str).replace('nan', '')

    def get_sql_data_types(self, profile: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate SQL data types based on the profile data.

        Args:
            profile (Dict[str, Any]): Profile data for the DataFrame.

        Returns:
            Dict[str, str]: Mapping of column names to SQL data types.
        """
        sql_types = {}
        for column, info in profile['full_profile'].items():
            if info['numeric']:
                if all(
                    float(x).is_integer()
                    for x in info['unique_values']
                    if x is not None and not pd.isna(x)
                ):
                    sql_types[column] = 'INTEGER'
                else:
                    sql_types[column] = 'FLOAT'
            elif info.get('date_detected', False):
                sql_types[column] = 'DATE'
            else:
                max_length = max(
                    len(str(x))
                    for x in info['unique_values']
                    if x is not None and not pd.isna(x)
                )
                sql_types[column] = f'VARCHAR({max_length})'
        return sql_types