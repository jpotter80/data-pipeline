# Data Pipeline Project

## Project Overview

This project is a comprehensive data pipeline designed to automate the process of ingesting CSV files, creating a PostgreSQL database, analyzing data structure using Generative AI, and generating insights. It streamlines the data analysis workflow, allowing analysts to quickly move from data gathering to actionable insights.


## Features

- Automatic CSV file detection and loading
- Dynamic database creation and table management
- AI-powered data analysis using LLM integration (via Anthropic API)
- SQL transformation generation for data cleaning and normalization
- Data visualization capabilities
- Comprehensive logging and output management
- Asynchronous execution for improved performance

## Project Structure

```
data-pipeline/
├── data_pipeline/
│   ├── analyze/
│   ├── ingest/
│   ├── cleaning/
│   ├── profiling/
│   ├── visualize/
│   └── config.py
├── dataset/
├── notebooks/
├── tests/
├── .env
├── .gitignore
├── main.py
├── README.md
├── poetry.lock
└── pyproject.toml
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/jpotter80/data-pipeline.git
   cd data-pipeline
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up environment variables in a `.env` file:
   ```
   DB_USER=your_postgres_username
   DB_PASS=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

4. Place your CSV files in the `dataset` directory.

## Usage

To run the entire pipeline:

```
poetry run python main.py
```

This will execute all steps of the pipeline, from data ingestion to insight generation.

## Current Development Focus

- Implementing SQL transformations for data cleaning and normalization
- Enhancing data visualization capabilities
- Developing a Jupyter notebook for step-by-step pipeline demonstration
- Implementing comprehensive error handling and recovery mechanisms
- Optimizing pipeline performance for larger datasets

## Planned Features

- Advanced data visualization and reporting
- Integration with pgvector for enhanced data analysis
- User interface for project and data parameter selection

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
