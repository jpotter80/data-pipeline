import os
from dotenv import load_dotenv
from data_pipeline.ingest.loader import CSVLoader, DBLoader
from data_pipeline.analyze.analyzer import LLMAnalyzer

# Load environment variables
load_dotenv()

def main():
    # Initialize components
    csv_loader = CSVLoader()
    db_name = csv_loader.get_database_name()
    db_loader = DBLoader(db_name)
    llm_analyzer = LLMAnalyzer()

    # Create the database (if it doesn't exist)
    db_loader.create_database()

    # Process all CSV files
    csv_analyses = csv_loader.process_all_csv()

    for csv_analysis in csv_analyses:
        filename = csv_analysis['filename']
        analysis = csv_analysis['analysis']

        # Load CSV into DataFrame
        df = csv_loader.load_csv(filename)

        # Create table (if it doesn't exist) and insert data (if table is empty)
        table_name = os.path.splitext(filename)[0]  # Use filename without extension as table name
        db_loader.create_table(table_name, df)
        db_loader.insert_data(table_name, df)

        # Analyze with LLM (consider caching these results for efficiency)
        llm_analysis = llm_analyzer.analyze_structure(analysis)
        print(f"Analysis for {filename}:\n{llm_analysis}\n")

        # Generate SQL transformations (consider caching these results for efficiency)
        sql_transformations = llm_analyzer.generate_sql_transformations(llm_analysis)
        print(f"SQL Transformations for {filename}:\n{sql_transformations}\n")

        # TODO: Execute SQL transformations
        # TODO: Vectorize data
        # TODO: Generate insights
        # TODO: Visualize results

if __name__ == "__main__":
    main()