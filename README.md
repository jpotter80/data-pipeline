# Data Pipeline

A versatile data pipeline for CSV processing and analysis using PostgreSQL, OpenAI GPT-4o, and Python. This project automates the process of ingesting CSV files, creating a database, analyzing data structure, and generating insights using AI.

## Project Goals

- Create a flexible data pipeline that can handle various CSV files
- Automate the process of database creation, data ingestion, analysis, and transformation
- Utilize AI (GPT-4o) for data analysis and SQL query generation
- Provide a foundation for future enhancements such as data vectorization and visualization

## Features

- Automatic database creation based on CSV filename
- CSV file detection, loading, and table creation
- Data insertion into PostgreSQL
- AI-powered data analysis and SQL transformation generation
- Extensible architecture for future enhancements (vectorization, visualization)

## Prerequisites

- Python 3.9+
- PostgreSQL
- OpenAI API key

## Project Structure

```
data-pipeline/
├── data_pipeline/
│   ├── __init__.py
│   ├── ingest/
│   │   ├── __init__.py
│   │   └── loader.py
│   ├── analyze/
│   │   ├── __init__.py
│   │   └── analyzer.py
│   ├── transform/
│   │   ├── __init__.py
│   │   └── transformer.py
│   ├── vectorize/
│   │   ├── __init__.py
│   │   └── vectorizer.py
│   └── visualize/
│       ├── __init__.py
│       └── visualizer.py
├── dataset/
│   └── .gitkeep
├── tests/
│   └── __init__.py
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/data-pipeline.git
   cd data-pipeline
   ```

2. Install Poetry:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```
   poetry install
   ```

4. Create a `.env` file in the project root and add your environment variables:
   ```
   DB_USER=your_postgres_username
   DB_PASS=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Ensure PostgreSQL is installed and running on your system.

## Usage

1. Place your CSV file in the `dataset` directory. The name of the CSV file (without extension) will be used as the database name.

2. Run the main script:
   ```
   poetry run python main.py
   ```

   This will:
   - Create a new PostgreSQL database with the same name as your CSV file (without extension)
   - Load the CSV data into a table in this database
   - Perform analysis and generate insights

Note: If you place multiple CSV files in the dataset directory, the name of the first CSV file (alphabetically) will be used as the database name, and all CSV files will be loaded as separate tables in this database.

## Components

### Ingest

The `ingest` module (`data_pipeline/ingest/loader.py`) contains two main classes:

- `CSVLoader`: Handles loading and analyzing CSV files from the `dataset` directory.
- `DBLoader`: Manages database operations, including database creation, table creation, and data insertion.

### Analyze

The `analyze` module (`data_pipeline/analyze/analyzer.py`) contains the `LLMAnalyzer` class, which uses OpenAI's GPT-4o to:

- Analyze the structure of CSV files
- Generate SQL transformations based on the analysis

### Transform, Vectorize, and Visualize

These modules are placeholders for future enhancements:

- `transform`: Will implement SQL transformations generated by the analyzer.
- `vectorize`: Will handle data vectorization for advanced analytics.
- `visualize`: Will create visualizations of the processed data and insights.

## Development

To contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run tests (`poetry run pytest`)
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Create a new Pull Request

To add new development dependencies, use:
```
poetry add --group dev <package-name>
```

## Testing

Currently, the `tests/` directory is empty. As you develop the project, add unit tests for each module to ensure functionality and make future modifications easier.

## Future Enhancements

- Implement SQL transformation execution in the `transform` module
- Add data vectorization using pgai in the `vectorize` module
- Develop insight generation and visualization components in the `visualize` module
- Add comprehensive error handling and logging throughout the pipeline
- Expand test coverage with unit and integration tests
- Implement parallel processing for handling large datasets
- Add support for different database backends
- Create a web interface for monitoring and controlling the pipeline
- Enhance multi-file handling to allow users to specify a common database name
- Implement error handling for invalid database names (e.g., CSV files with spaces or special characters)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.