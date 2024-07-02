# Data Pipeline

A versatile data pipeline for CSV processing, analysis, and transformation using PostgreSQL, OpenAI GPT-4, and Python.

## Project Overview

This project automates the process of ingesting CSV files, creating a PostgreSQL database, analyzing data structure using llm's, and generating SQL transformations for data cleaning and normalization.

## Features

- Automatic CSV file detection and loading
- Dynamic database and table creation based on CSV filename
- Data insertion into PostgreSQL
- LLM-powered data analysis using OpenAI's GPT-4
- SQL transformation generation for data cleaning and normalization
- Extensible architecture for future enhancements (vectorization, visualization)

## Prerequisites

- Python 3.12+
- PostgreSQL
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/jpotter80/data-pipeline.git
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

## Usage

1. Place your CSV file(s) in the `dataset` directory. The name of the first CSV file (alphabetically) will be used as the database name.

2. Run the main script:
   ```
   poetry run python main.py
   ```

   This will:
   - Create a new PostgreSQL database (if it doesn't exist)
   - Create tables based on CSV files (if they don't exist)
   - Insert data into the tables (if they're empty)
   - Perform AI-powered analysis of the data structure
   - Generate SQL transformations for data cleaning and normalization

## Project Structure

```
data-pipeline/
├── data_pipeline/
│   ├── ingest/
│   │   ├── loader.py
│   ├── analyze/
│   │   ├── analyzer.py
│   ├── transform/
│   │   ├── transformer.py (TODO)
│   ├── vectorize/
│   │   ├── vectorizer.py (TODO)
│   └── visualize/
│       ├── visualizer.py (TODO)
├── dataset/
│   └── .gitkeep
├── tests/
│   └── __init__.py (TODO: Add unit tests)
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```

## Components

### Ingest

The `ingest` module (`data_pipeline/ingest/loader.py`) handles CSV loading and database operations.

### Analyze

The `analyze` module (`data_pipeline/analyze/analyzer.py`) uses OpenAI's GPT-4 to analyze data structure and generate SQL transformations.

### Transform, Vectorize, and Visualize

These modules are placeholders for future enhancements.

## Future Enhancements

- Implement SQL transformation execution
- Add data vectorization for advanced analytics
- Develop insight generation and visualization components
- Implement caching for LLM analyses and SQL transformations
- Add comprehensive error handling and logging
- Expand test coverage with unit and integration tests
- Implement parallel processing for handling large datasets
- Create a web interface for monitoring and controlling the pipeline

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
