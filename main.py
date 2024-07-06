"""
Main module for the data pipeline project.
"""

import asyncio
import logging
from pathlib import Path
from typing import List, Tuple, Optional

from data_pipeline.config import Config
from data_pipeline.profiling.profiler import DataProfiler
from data_pipeline.cleaning.cleaner import DataCleaner
from data_pipeline.ingest.loader import CSVLoader, DBLoader
from data_pipeline.analyze.analyzer import LLMAnalyzer
from data_pipeline.visualize.visualizer import Visualizer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def process_csv(
    csv_loader: CSVLoader,
    db_loader: DBLoader,
    llm_analyzer: LLMAnalyzer,
    visualizer: Visualizer,
    profiler: DataProfiler,
    cleaner: DataCleaner,
    db_name: str,
    filename: str
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    try:
        file_path = Path(csv_loader.data_dir) / filename
        logger.info(f"Processing file: {file_path}")

        profile = await profiler.profile_csv(str(file_path))
        report = profiler.generate_report(profile)
        logger.info(f"Profiling report for {filename}:\n{report}")

        df = await csv_loader.load_csv(filename)
        if df is None:
            logger.error(f"Failed to load {filename}")
            return None, None, None

        cleaned_df = await cleaner.clean_data(df, profile)
        sql_data_types = cleaner.get_sql_data_types(profile)

        table_name = Path(filename).stem.lower()
        await db_loader.create_table(db_name, table_name, cleaned_df, sql_data_types)
        await db_loader.insert_data(db_name, table_name, cleaned_df, sql_data_types)

        llm_analysis, analysis_log = await llm_analyzer.analyze_structure(profile)
        logger.info(f"Analysis for {filename}:\n{llm_analysis}")
        logger.info(f"Analysis log saved to: {analysis_log}")

        sql_transformations, sql_log = await llm_analyzer.generate_sql_transformations(llm_analysis)
        logger.info(f"SQL Transformations for {filename}:\n{sql_transformations}")
        logger.info(f"SQL transformations log saved to: {sql_log}")

        vis_filename = await visualizer.create_visualizations(cleaned_df, table_name)
        logger.info(f"Visualizations saved to: {vis_filename}")

        return table_name, llm_analysis, sql_transformations

    except Exception as e:
        logger.exception(f"Error processing {filename}: {str(e)}")
        return None, None, None

async def main():
    try:
        config = Config()
        csv_loader = CSVLoader(config.data_dir)
        db_loader = DBLoader(config.db_config)
        llm_analyzer = LLMAnalyzer(config.anthropic_api_key)
        visualizer = Visualizer(config.output_dir)
        profiler = DataProfiler()
        cleaner = DataCleaner()

        csv_files = csv_loader.get_csv_files()
        if not csv_files:
            logger.error("No CSV files found in the dataset directory.")
            return

        db_name = await db_loader.get_or_create_database(csv_files)
        if not db_name:
            logger.error("Failed to create or get a database.")
            return

        logger.info(f"Using database: {db_name}")

        tasks = [
            process_csv(csv_loader, db_loader, llm_analyzer, visualizer, profiler, cleaner, db_name, filename)
            for filename in csv_files
        ]
        results = await asyncio.gather(*tasks)

        for table_name, _, _ in results:
            if table_name:
                logger.info(f"Processed table: {table_name}")
            else:
                logger.warning("Failed to process a CSV file")

    except Exception as e:
        logger.exception(f"An error occurred in the main function: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())