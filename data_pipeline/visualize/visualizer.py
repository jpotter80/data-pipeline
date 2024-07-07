import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import logging
import aiofiles

logger = logging.getLogger(__name__)

class Visualizer:
    def __init__(self, output_dir='visualizations'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    async def create_visualizations(self, df: pd.DataFrame, table_name: str) -> str:
        try:
            numeric_df = df.select_dtypes(include=['int64', 'float64'])
            if numeric_df.empty:
                logger.warning(f"No numeric columns found in {table_name}. Skipping visualizations.")
                return None

            # Create a correlation heatmap for numeric columns
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
            plt.title(f"Correlation Heatmap for {table_name}")
            plt.tight_layout()
            
            # Save the plot asynchronously
            filename = os.path.join(self.output_dir, f"{table_name}_correlation_heatmap.png")
            plt.savefig(filename)
            plt.close()

            logger.info(f"Visualization created for {table_name}")
            return filename
        except Exception as e:
            logger.error(f"Error creating visualization for {table_name}: {str(e)}")
            return None

    def _create_summary_stats(self, df: pd.DataFrame, table_name: str):
        numeric_df = df.select_dtypes(include=['int64', 'float64'])
        if not numeric_df.empty:
            plt.figure(figsize=(10, 6))
            sns.heatmap(numeric_df.describe().transpose(), annot=True, cmap="YlGnBu")
            plt.title(f"Summary Statistics for {table_name}")
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, f"{table_name}_summary_stats.png"))
            plt.close()

    def _create_correlation_heatmap(self, df: pd.DataFrame, table_name: str):
        numeric_df = df.select_dtypes(include=['int64', 'float64'])
        if not numeric_df.empty:
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
            plt.title(f"Correlation Heatmap for {table_name}")
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, f"{table_name}_correlation_heatmap.png"))
            plt.close()

    def _create_histograms(self, df: pd.DataFrame, table_name: str):
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        for col in numeric_cols:
            plt.figure(figsize=(8, 6))
            sns.histplot(df[col], kde=True)
            plt.title(f"Distribution of {col} in {table_name}")
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, f"{table_name}_{col}_histogram.png"))
            plt.close()

    def _create_box_plots(self, df: pd.DataFrame, table_name: str):
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        if not numeric_cols.empty:
            plt.figure(figsize=(12, 6))
            df[numeric_cols].boxplot()
            plt.title(f"Box Plots for Numeric Columns in {table_name}")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, f"{table_name}_box_plots.png"))
            plt.close()

    def _create_bar_plots(self, df: pd.DataFrame, table_name: str):
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            plt.figure(figsize=(10, 6))
            value_counts = df[col].value_counts()
            if len(value_counts) > 20:  # If too many categories, only plot top 20
                value_counts = value_counts.nlargest(20)
            value_counts.plot(kind='bar')
            plt.title(f"Distribution of {col} in {table_name}")
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, f"{table_name}_{col}_bar_plot.png"))
            plt.close()